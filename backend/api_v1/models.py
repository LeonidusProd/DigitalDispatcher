from django.db import models
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver


class City(models.Model):
    name = models.CharField(max_length=40, null=False, unique=True, verbose_name='Название')

    def __str__(self):
        return f'Город {self.name}'

    def short_str(self):
        return f'г. {self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Street(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, verbose_name='Город')
    name = models.CharField(max_length=100, null=False, verbose_name='Улица')

    def __str__(self):
        return f'{self.city.__str__()}, улица {self.name}'

    def short_str(self):
        return f'ул. {self.name}'

    def short_str_with_city(self):
        return f'{self.city.short_str()}, ул. {self.name}'

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'


class Building(models.Model):
    street = models.ForeignKey(Street, on_delete=models.CASCADE, null=False, verbose_name='Улица')
    number = models.IntegerField(null=False, verbose_name='Номер здания')
    corpus = models.CharField(max_length=5, null=True, blank=True, verbose_name='Корпус')

    def __str__(self):
        corp = ''
        if self.corpus:
            corp = f', корпус {self.corpus}'
        return f'{self.street.__str__()}, дом {self.number}{corp}'

    def short_str(self):
        corp = ''
        if self.corpus:
            corp = f'/{self.corpus}'
        return f'{self.street.short_str()}, д. {self.number}{corp}'

    def short_str_with_city(self):
        corp = ''
        if self.corpus:
            corp = f'/{self.corpus}'
        return f'{self.street.short_str_with_city()}, д. {self.number}{corp}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


@receiver(pre_save, sender=Building)
def check_unique_building(sender, instance, **kwargs):
    # Проверка уникальности комбинации номера и корпуса для каждой улицы перед сохранением объекта Building
    if Building.objects.filter(street=instance.street, number=instance.number, corpus=instance.corpus).exists():
        raise ValidationError("Здание с таким номером и корпусом уже существует на этой улице.")


class WorkSchedule(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Название графика работы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'


class WorkDay(models.Model):
    DAY_CHOICES = (
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Четверг'),
        (5, 'Пятница'),
        (6, 'Суббота'),
        (7, 'Воскресенье'),
    )
    schedule = models.ForeignKey(
        WorkSchedule, on_delete=models.CASCADE, related_name='work_days', null=False, verbose_name='График работы'
    )
    day_of_week = models.IntegerField(choices=DAY_CHOICES, null=False, verbose_name='День недели')
    is_not_working = models.BooleanField(default=False, null=False, verbose_name='Нерабочий')
    start_time = models.TimeField(null=True, blank=True, verbose_name='Время начала работы')
    end_time = models.TimeField(null=True, blank=True, verbose_name='Время конца работы')

    # def __str__(self):
    #     if self.is_not_working:
    #         end = ' не рабочий'
    #     else:
    #         end = f' c {self.start_time} до {self.end_time}'
    #     return f'{self.schedule.name}: {self.get_day_of_week_display}{end}'

    def short_str(self):
        if self.is_not_working:
            end = ' не рабочий'
        else:
            end = f' c {self.start_time} до {self.end_time}'
        return f'{self.get_day_of_week_display()}{end}'

    class Meta:
        verbose_name = 'Рабочий день'
        verbose_name_plural = 'Рабочие дни'


@receiver(post_save, sender=WorkSchedule)
def create_work_days(sender, instance, created, **kwargs):
    if created:
        for day_of_week in range(1, 8):
            WorkDay.objects.create(schedule=instance, day_of_week=day_of_week, is_not_working=True)
        # WorkDay.objects.create(user=instance, is_performer=True)


class Office(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Название УК')
    address = models.ForeignKey(Building, on_delete=models.CASCADE, null=False, verbose_name='Адрес офиса УК')
    work_schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE, null=False, verbose_name='График работы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Управляющая компания'
        verbose_name_plural = 'Управляющие компании'


class HousingComplex(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Название ЖК')
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=False, verbose_name='Офис УК')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жилой комплекс'
        verbose_name_plural = 'Жилые комплексы'


class House(models.Model):
    complex = models.ForeignKey(HousingComplex, on_delete=models.CASCADE, null=False, verbose_name='Жилой комплекс')
    address = models.ForeignKey(Building, on_delete=models.CASCADE, null=False, verbose_name='Адрес')

    def __str__(self):
        return f'{self.complex.__str__()}: {self.address.short_str_with_city()}'

    def short_str(self):
        return f'{self.address.short_str()}'

    class Meta:
        verbose_name = 'Жилой дом'
        verbose_name_plural = 'Жилые дома'


class Resident(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Имя')
    surname = models.CharField(max_length=50, null=False, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=15, null=False, verbose_name='Номер телефона')
    tg_id = models.BigIntegerField(unique=True, null=True, blank=True, verbose_name='ID пользователя в Telegram')

    def __str__(self):
        if self.patronymic:
            return f'{self.surname} {self.name} {self.patronymic}'
        else:
            return f'{self.surname} {self.name}'

    def get_respectful_treatment(self):
        if self.patronymic:
            return f'{self.name} {self.patronymic}'
        else:
            return f'{self.name}'

    class Meta:
        verbose_name = 'Житель'
        verbose_name_plural = 'Жители'


class ExecutionStatus(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус выполнения'
        verbose_name_plural = 'Статусы выполнения'


class Department(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Отдел')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Position(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Должность')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False, verbose_name='Отдел')

    def __str__(self):
        return f'{self.department.__str__()}: {self.name}'

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Employee(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Имя')
    surname = models.CharField(max_length=50, null=False, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, null=False, verbose_name='Отчество')
    phone = models.CharField(max_length=15, null=False, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта', null=True, blank=True)
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Управляющая компания')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=False, verbose_name='Должность')
    tg_id = models.BigIntegerField(unique=True, null=True, blank=True, verbose_name='ID пользователя в Telegram')

    def __str__(self):
        if self.office:
            return f'УК {self.office.name}: {self.surname} {self.name} {self.patronymic}'
        else:
            return f'{self.surname} {self.name} {self.patronymic}'

    def get_full_SNP(self):
        if self.patronymic:
            return f'{self.surname} {self.name} {self.patronymic}'
        else:
            return f'{self.surname} {self.name}'

    def get_respectful_treatment(self):
        if self.patronymic:
            return f'{self.name} {self.patronymic}'
        else:
            return f'{self.name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Service(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Типовая задача')
    description = models.TextField(null=False, verbose_name='Описание задачи')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=False,
                                 verbose_name='Требуемая должность исполнителя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Типовая задача'
        verbose_name_plural = 'Типовые задачи'


def get_request_photo_path(instance, filename=None):
    return f'request/{instance.resident.tg_id}/{filename}'


class Request(models.Model):
    created_at = models.DateTimeField(null=False, verbose_name='Дата и время создания', auto_now_add=True)
    text = models.TextField(null=False, verbose_name='Текст обращения')
    status = models.ForeignKey(ExecutionStatus, on_delete=models.CASCADE, null=False, verbose_name='Статус выполнения')
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, null=False, verbose_name='Автор заявки')
    address = models.ForeignKey(House, on_delete=models.CASCADE, null=False, verbose_name='Адрес заявки')
    apartment = models.IntegerField(null=True, blank=True, verbose_name='Номер квартиры')
    photo = models.ImageField(upload_to=get_request_photo_path, null=True, blank=True, verbose_name='Фото обращения')
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True,
    # verbose_name='Исполнитель') service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True,
    # blank=True, verbose_name='Задача')

    def __str__(self):
        local_time = timezone.localtime(self.created_at, timezone.get_current_timezone())
        return f'{local_time}: {self.address} - {self.status}'

    class Meta:
        verbose_name = 'Заявка/Обращение'
        verbose_name_plural = 'Заявки/Обращения'


class RequestTask(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, null=False, verbose_name='Заявка')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, verbose_name='Исполнитель')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=False, verbose_name='Задача')
    status = models.ForeignKey(ExecutionStatus, on_delete=models.CASCADE, null=False, verbose_name='Статус выполнения')

    # def __str__(self):
    #     return

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class BotsSettings(models.Model):
    residentBotToken = models.TextField(null=False, verbose_name='Токен бота жителей')
    staffBotToken = models.TextField(null=False, verbose_name='Токен бота мастеров')

    class Meta:
        verbose_name = 'Токены ботов'
        verbose_name_plural = 'Токены ботов'


class TemporaryToken(models.Model):
    token = models.CharField(max_length=100, unique=True)
    created_to = models.BigIntegerField(unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return timezone.now() - self.created_at < timedelta(minutes=15)  # Токен действителен 15 минут
