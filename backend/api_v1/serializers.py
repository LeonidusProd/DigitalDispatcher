from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


# Используемые
class BuildingLstSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка всех адресов (жилые и не жилые здания)
    """

    name = serializers.SerializerMethodField(method_name='get_name')

    @staticmethod
    def get_name(obj): return str(obj.short_str_with_city())

    class Meta:
        model = Building
        fields = ['pk', 'name']


class BuildingCrtDelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания и удаления адреса
    """

    class Meta:
        model = Building
        fields = '__all__'


class BotTokensSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения и изменения настроек ботов
    """

    class Meta:
        model = BotsSettings
        fields = '__all__'


class CityLstCrtSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка всех городов и добавления нового города
    """

    class Meta:
        model = City
        fields = ['pk', 'name']


class StreetLstCrtSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка улиц города и добавления новой улицы
    """

    class Meta:
        model = Street
        fields = ['pk', 'city', 'name']


class HousingComplexLstCrtDelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка всех ЖК, создания и удаления ЖК
    """

    class Meta:
        model = HousingComplex
        fields = ['pk', 'name', 'office']


class DepartmentLstCrtDelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка всех отделов, создания и удаления отдела
    """

    class Meta:
        model = Department
        fields = ['pk', 'name']


class EmployeeLstSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка всех сотрудников
    """

    name = serializers.SerializerMethodField(method_name='get_name')
    empl_name = serializers.SerializerMethodField(method_name='get_empl_name')
    empl_surname = serializers.SerializerMethodField(method_name='get_empl_surname')

    @staticmethod
    def get_name(obj):
        return f'{obj.surname} {obj.name} {obj.patronymic}'.strip()

    @staticmethod
    def get_empl_name(obj):
        return obj.name

    @staticmethod
    def get_empl_surname(obj):
        return obj.surname

    class Meta:
        model = Employee
        fields = ['pk', 'name', 'empl_name', 'empl_surname']


class EmployeeCrtDelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для добавления и удаления сотрудника
    """

    class Meta:
        model = Employee
        fields = '__all__'


class HouseLstCrtDelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка всех жилых домов, создания и удаления жилого дома
    """

    name = serializers.SerializerMethodField(method_name='get_name')

    @staticmethod
    def get_name(obj):
        return str(obj.__str__())

    class Meta:
        model = House
        fields = ['pk', 'name', 'complex', 'address']


class ComplexHousesLstSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка домов жилого комплекса
    """

    name = serializers.SerializerMethodField(method_name='get_name')

    @staticmethod
    def get_name(obj):
        return str(obj.short_str())

    class Meta:
        model = House
        fields = ['pk', 'name', 'complex', 'address']


class OfficeLstCrtDelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка всех УК, создания и удаления УК
    """

    class Meta:
        model = Office
        fields = ['pk', 'name', 'address', 'work_schedule']


class PositionLstCrtDelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка всех должностей, создания и удаления должности
    """

    class Meta:
        model = Position
        fields = ['pk', 'name', 'department']


class RequestShortInfoSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка заявок (новых или активных)
    с короткой информацией
    """

    date = serializers.SerializerMethodField(method_name='get_date')
    info = serializers.SerializerMethodField(method_name='get_info')
    address = serializers.SerializerMethodField(method_name='get_address')

    @staticmethod
    def get_date(obj):
        local_time = timezone.localtime(obj.created_at, timezone.get_current_timezone())
        return f"{local_time.date().strftime('%d.%m.%Y')} {local_time.time().strftime('%H:%M')}"

    @staticmethod
    def get_info(obj):
        return obj.text

    @staticmethod
    def get_address(obj):
        return obj.address.address.short_str()

    class Meta:
        model = Request
        fields = ['pk', 'date', 'address', 'info']


class RequestDetSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения польной информации о заявке и получения списка заявок от пользователя TG
    """

    info = serializers.SerializerMethodField(method_name='get_info')
    date = serializers.SerializerMethodField(method_name='get_date')
    complex = serializers.SerializerMethodField(method_name='get_complex')
    status_name = serializers.SerializerMethodField(method_name='get_status_name', read_only=True)
    address = serializers.SerializerMethodField(method_name='get_address')
    resident = serializers.SerializerMethodField(method_name='get_resident')
    office_id = serializers.SerializerMethodField(method_name='get_office_id')

    @staticmethod
    def get_info(obj):
        return obj.text

    @staticmethod
    def get_date(obj):
        local_time = timezone.localtime(obj.created_at, timezone.get_current_timezone())
        return f"{local_time.date().strftime('%d.%m.%Y')} {local_time.time().strftime('%H:%M')}"

    @staticmethod
    def get_complex(obj):
        return obj.address.complex.__str__()

    @staticmethod
    def get_status_name(obj):
        return obj.status.name

    @staticmethod
    def get_address(obj):
        if obj.apartment:
            return f"{obj.address.address.short_str()}, кв. {obj.apartment}"
        else:
            return f"{obj.address.address.short_str()}"

    @staticmethod
    def get_resident(obj):
        return obj.resident.__str__()

    @staticmethod
    def get_office_id(obj):
        return obj.address.complex.office.pk

    class Meta:
        model = Request
        fields = ['pk', 'info', 'date', 'status_name', 'status', 'resident', 'address', 'complex', 'photo', 'office_id']


class RequestTaskInfoSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка задач у заявки и списка задач для пользователя TG
    """

    employee = serializers.SerializerMethodField(method_name='get_employee')
    task = serializers.SerializerMethodField(method_name='get_task')
    status = serializers.SlugRelatedField(slug_field='name', read_only=True)

    @staticmethod
    def get_employee(obj):
        return obj.employee.get_respectful_treatment()

    @staticmethod
    def get_task(obj):
        return obj.service.name

    class Meta:
        model = RequestTask
        fields = ['pk', 'employee', 'task', 'status']


class RequestCrtSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания новой заявки
    """

    class Meta:
        model = Request
        fields = '__all__'


class WorkScheduleLstSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка графиков работы
    """

    work_days = serializers.SerializerMethodField(method_name='get_work_days')

    @staticmethod
    def get_work_days(obj):
        work_days = obj.work_days.all().order_by('day_of_week')
        serializer = WorkDayShortLstSerializer(work_days, many=True)
        return serializer.data

    class Meta:
        model = WorkSchedule
        fields = ['pk', 'name', 'work_days']


class WorkScheduleDetMngSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения полной информации о графике работы
    """

    work_days = serializers.SerializerMethodField(method_name='get_work_days')

    @staticmethod
    def get_work_days(obj):
        work_days = obj.work_days.all().order_by('day_of_week')
        serializer = WorkDayFullLstSerializer(work_days, many=True)
        return serializer.data

    class Meta:
        model = WorkSchedule
        fields = ['id', 'name', 'work_days']


class WorkDayFullLstSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка дней графика работы с полной информацией
    и изменения информации о рабочем дне
    """

    day_of_week_name = serializers.ChoiceField(
        choices=WorkDay.DAY_CHOICES,
        source='get_day_of_week_display',
        read_only=True
    )
    day_of_week = serializers.ChoiceField(choices=WorkDay.DAY_CHOICES, read_only=True)
    resume = serializers.SerializerMethodField(method_name='get_resume')

    @staticmethod
    def get_resume(obj):
        return str(obj.short_str())

    class Meta:
        model = WorkDay
        fields = ['id', 'day_of_week', 'day_of_week_name', 'is_not_working', 'start_time', 'end_time', 'resume']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['is_not_working']:
            data.pop('start_time', None)
            data.pop('end_time', None)
        return data


class WorkScheduleCrtDelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания и удаления графика работы
    """

    class Meta:
        model = WorkSchedule
        fields = '__all__'


class ServiceLstCrtDelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка всех типовых задач, создания и удаления типовой задачи
    """

    class Meta:
        model = Service
        fields = ['pk', 'name', 'description', 'position']


class ServiseEmployeesSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка сотрудников, подходящих к задаче
    """

    name = serializers.SerializerMethodField(method_name='get_name')

    @staticmethod
    def get_name(obj):
        return obj.get_full_SNP()

    class Meta:
        model = Employee
        fields = ['pk', 'name']


class TaskFullInfoSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения и изменения задачи для заявки
    """

    employee = serializers.SerializerMethodField(method_name='get_employee')
    task = serializers.SerializerMethodField(method_name='get_task')
    status_name = serializers.SerializerMethodField(method_name='get_status_name')
    task_description = serializers.SerializerMethodField(method_name='get_task_description')

    @staticmethod
    def get_employee(obj):
        return obj.employee.get_respectful_treatment()

    @staticmethod
    def get_task(obj):
        return obj.service.name

    @staticmethod
    def get_status_name(obj):
        return obj.status.name

    @staticmethod
    def get_task_description(obj):
        return obj.service.description

    class Meta:
        model = RequestTask
        fields = ['pk', 'employee', 'task', 'status', 'status_name', 'request', 'task_description']


class RequestTaskDelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания и удаления задачи для заявки
    """

    class Meta:
        model = RequestTask
        fields = '__all__'


class ResidentLstSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка всех жителей и информации о жителе по TG user id
    """

    name = serializers.SerializerMethodField(method_name='get_name')

    @staticmethod
    def get_name(obj):
        return obj.__str__()

    class Meta:
        model = Resident
        fields = ['pk', 'name']


class ResidentCrtSerializer(serializers.ModelSerializer):
    """
    Сериализатор для добавления нового жителя
    """

    class Meta:
        model = Resident
        fields = ['pk', 'name', 'surname', 'patronymic', 'phone', 'tg_id']


class WorkDayShortLstSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка дней графика работы с сокращённой информацией
    """

    resume = serializers.SerializerMethodField(method_name='get_resume')

    @staticmethod
    def get_resume(obj):
        return str(obj.short_str())

    class Meta:
        model = WorkDay
        fields = ['id', 'resume']


class UserLstMngCrtDelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка всех пользователей, создания и удаления пользователя
    """

    name = serializers.SerializerMethodField(method_name='get_name')

    @staticmethod
    def get_name(obj):
        if obj.is_superuser:
            return f'{obj.username}: Администратор'
        elif obj.is_staff and obj.is_superuser:
            return f'{obj.username}: Администратор'
        elif obj.is_staff:
            return f'{obj.username}: Персонал'

    class Meta:
        model = User
        fields = ['pk', 'name', 'username', 'password', 'is_superuser', 'is_staff', 'first_name', 'last_name', ]
