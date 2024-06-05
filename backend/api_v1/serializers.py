from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *
from django.contrib.auth.models import User


'''
Lst - List
Det - Detail
Mng - Manage
Crt - Create
Del - Delete
'''


# Используемые
class BuildingLstSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    def get_name(self, obj): return str(obj.short_str_with_city())

    class Meta:
        model = Building
        fields = ['pk', 'name']


class BuildingLstMngCrtDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class BotTokensSerializer(serializers.ModelSerializer):

    class Meta:
        model = BotsSettings
        fields = '__all__'


class CityLstMngCrtDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['pk', 'name']


class StreetLstMngCrtDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ['pk', 'city', 'name']


class HousingComplexLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = HousingComplex
        fields = ['pk', 'name', 'office']


class DepartmentUltimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['pk', 'name']


class EmployeeSpecSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')
    empl_name = serializers.SerializerMethodField(method_name='get_empl_name')
    empl_surname = serializers.SerializerMethodField(method_name='get_empl_surname')

    def get_name(self, obj):
        return f'{obj.surname} {obj.name} {obj.patronymic}'.strip()

    def get_empl_name(self, obj):
        return obj.name

    def get_empl_surname(self, obj):
        return obj.surname

    class Meta:
        model = Employee
        fields = ['pk', 'name', 'empl_name', 'empl_surname']


class EmployeeFullLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class HouseLstMngCrtDelSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    def get_name(self, obj):
        return str(obj.__str__())

    class Meta:
        model = House
        fields = ['pk', 'name', 'complex', 'address']


class HouseShortLstSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    def get_name(self, obj):
        return str(obj.short_str())

    class Meta:
        model = House
        fields = ['pk', 'name', 'complex', 'address']


class OfficeLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Office
        fields = ['pk', 'name', 'address', 'work_schedule']


class PositionLstMngCrtDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['pk', 'name', 'department']


class RequestShortInfoSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField(method_name='get_date')
    info = serializers.SerializerMethodField(method_name='get_info')
    address = serializers.SerializerMethodField(method_name='get_address')

    def get_date(self, obj):
        local_time = timezone.localtime(obj.created_at, timezone.get_current_timezone())
        return f"{local_time.date().strftime('%d.%m.%Y')} {local_time.time().strftime('%H:%M')}"

    def get_info(self, obj):
        return obj.text

    def get_address(self, obj):
        return obj.address.address.short_str()

    class Meta:
        model = Request
        fields = ['pk', 'date', 'address', 'info']


class RequestDetSerializer(serializers.ModelSerializer):
    info = serializers.SerializerMethodField(method_name='get_info')
    date = serializers.SerializerMethodField(method_name='get_date')
    complex = serializers.SerializerMethodField(method_name='get_complex')
    status_name = serializers.SerializerMethodField(method_name='get_status_name', read_only=True)
    address = serializers.SerializerMethodField(method_name='get_address')
    resident = serializers.SerializerMethodField(method_name='get_resident')
    office_id = serializers.SerializerMethodField(method_name='get_office_id')

    def get_info(self, obj):
        return obj.text

    def get_date(self, obj):
        local_time = timezone.localtime(obj.created_at, timezone.get_current_timezone())
        return f"{local_time.date().strftime('%d.%m.%Y')} {local_time.time().strftime('%H:%M')}"

    def get_complex(self, obj):
        return obj.address.complex.__str__()

    def get_status_name(self, obj):
        return obj.status.name

    def get_address(self, obj):
        if obj.apartment:
            return f"{obj.address.address.short_str()}, кв. {obj.apartment}"
        else:
            return f"{obj.address.address.short_str()}"

    def get_resident(self, obj):
        return obj.resident.__str__()

    def get_office_id(self, obj):
        return obj.address.complex.office.pk

    class Meta:
        model = Request
        fields = ['pk', 'info', 'date', 'status_name', 'status', 'resident', 'address', 'complex', 'photo', 'office_id']


class RequestTaskInfoSerializer(serializers.ModelSerializer):
    employee = serializers.SerializerMethodField(method_name='get_employee')
    task = serializers.SerializerMethodField(method_name='get_task')
    status = serializers.SlugRelatedField(slug_field='name', read_only=True)

    def get_employee(self, obj):
        return obj.employee.get_respectful_treatment()

    def get_task(self, obj):
        return obj.service.name

    class Meta:
        model = RequestTask
        fields = ['pk', 'employee', 'task', 'status']


class RequestLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'


class WorkScheduleLstSerializer(serializers.ModelSerializer):
    work_days = serializers.SerializerMethodField()

    def get_work_days(self, obj):
        work_days = obj.work_days.all().order_by('day_of_week')
        serializer = WorkDayShortLstSerializer(work_days, many=True)
        # serializer = WorkDayFullLstSerializer(work_days, many=True)
        return serializer.data

    class Meta:
        model = WorkSchedule
        fields = ['pk', 'name', 'work_days']


class WorkScheduleDetMngSerializer(serializers.ModelSerializer):
    work_days = serializers.SerializerMethodField()

    def get_work_days(self, obj):
        work_days = obj.work_days.all().order_by('day_of_week')
        serializer = WorkDayFullLstSerializer(work_days, many=True)
        return serializer.data

    class Meta:
        model = WorkSchedule
        fields = ['id', 'name', 'work_days']


class WorkDayFullLstSerializer(serializers.ModelSerializer):
    day_of_week_name = serializers.ChoiceField(choices=WorkDay.DAY_CHOICES, source='get_day_of_week_display', read_only=True)
    day_of_week = serializers.ChoiceField(choices=WorkDay.DAY_CHOICES, read_only=True)
    resume = serializers.SerializerMethodField(method_name='get_resume')

    def get_resume(self, obj):
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

    class Meta:
        model = WorkSchedule
        fields = '__all__'


class ServiceLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['pk', 'name', 'description', 'position']


class ServiseEmployeesSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    def get_name(self, obj):
        return obj.get_full_SNP()

    class Meta:
        model = Employee
        fields = ['pk', 'name']


class TaskFullInfoSerializer(serializers.ModelSerializer):
    employee = serializers.SerializerMethodField(method_name='get_employee')
    task = serializers.SerializerMethodField(method_name='get_task')
    status_name = serializers.SerializerMethodField(method_name='get_status_name')
    task_description = serializers.SerializerMethodField(method_name='get_task_description')

    def get_employee(self, obj):
        return obj.employee.get_respectful_treatment()

    def get_task(self, obj):
        return obj.service.name

    def get_status_name(self, obj):
        return obj.status.name

    def get_task_description(self, obj):
        return obj.service.description

    class Meta:
        model = RequestTask
        fields = ['pk', 'employee', 'task', 'status', 'status_name', 'request', 'task_description']


class RequestTaskDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestTask
        fields = '__all__'


class ResidentLstSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    def get_name(self,obj):
        return obj.__str__()

    class Meta:
        model = Resident
        fields = ['pk', 'name']


class ResidentFullLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resident
        fields = ['pk', 'name', 'surname', 'patronymic', 'phone', 'tg_id']


class WorkDayShortLstSerializer(serializers.ModelSerializer):
    resume = serializers.SerializerMethodField(method_name='get_resume')

    def get_resume(self, obj):
        return str(obj.short_str())

    class Meta:
        model = WorkDay
        fields = ['id', 'resume']


class UserLstMngCrtDelSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    def get_name(self, obj):
        if obj.is_superuser:
            return f'{obj.username}: Администратор'
        elif obj.is_staff and obj.is_superuser:
            return f'{obj.username}: Администратор'
        elif obj.is_staff:
            return f'{obj.username}: Персонал'

    class Meta:
        model = User
        fields = ['pk', 'name', 'username', 'password', 'is_superuser', 'is_staff', 'first_name', 'last_name', ]


# Специализированные serializer
class TemporaryTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporaryToken
        fields = ['token', 'created_to', 'created_at']


# Не используются в настоящий момент
# class CityDetSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField(method_name='get_full_name')
#     short_full_name = serializers.SerializerMethodField(method_name='get_short_full_name')
#
#     def get_full_name(self, obj):
#         return str(obj)
#
#     def get_short_full_name(self, obj):
#         return obj.short_str()
#
#     class Meta:
#         model = City
#         fields = ['id', 'name', 'full_name', 'short_full_name']
#
# #####################################################################
#
# class StreetDetSerializer(serializers.ModelSerializer):
#     city_name = serializers.SerializerMethodField(method_name='get_city_name')
#     full_name = serializers.SerializerMethodField(method_name='get_full_name')
#     short_full_name = serializers.SerializerMethodField(method_name='get_short_full_name')
#
#     def get_city_name(self, obj): return str(obj.city.name)
#
#     def get_full_name(self, obj): return str(obj)
#
#     def get_short_full_name(self, obj): return obj.short_str()
#
#     class Meta:
#         model = Street
#         fields = ['id', 'name', 'city', 'city_name', 'full_name', 'short_full_name']
#
# #####################################################################
#
# class BuildingDetSerializer(serializers.ModelSerializer):
#     city_name = serializers.SerializerMethodField(method_name='get_city_name')
#     street_name = serializers.SerializerMethodField(method_name='get_street_name')
#     full_name = serializers.SerializerMethodField(method_name='get_full_name')
#     short_full_name = serializers.SerializerMethodField(method_name='get_short_full_name')
#
#     def get_city_name(self, obj): return str(obj.street.city.name)
#
#     def get_street_name(self, obj): return str(obj.street.name)
#
#     def get_full_name(self, obj): return str(obj)
#
#     def get_short_full_name(self, obj): return obj.short_str()
#
#     class Meta:
#         model = Building
#         fields = ['id', 'street', 'city_name', 'street_name', 'number', 'corpus', 'full_name', 'short_full_name']
#
# #####################################################################
#
# #####################################################################
#
# class OfficeDetSerializer(serializers.ModelSerializer):
#     address_str = serializers.SerializerMethodField(method_name='get_address')
#     work_schedule_detail = serializers.SerializerMethodField(method_name='get_work_schedule')
#
#     def get_address(self, obj): return str(obj.address)
#
#     def get_work_schedule(self, obj):
#         work_days = WorkDay.objects.filter(schedule_id=obj.work_schedule).order_by('day_of_week')
#         serializer = WorkDayShortLstSerializer(work_days, many=True)
#         return serializer.data
#
#     class Meta:
#         model = Office
#         fields = ['id', 'name', 'address', 'address_str', 'work_schedule', 'work_schedule_detail']
#
# #####################################################################
#
# class HousingComplexDetSerializer(serializers.ModelSerializer):
#     office_name = serializers.SerializerMethodField(method_name='get_office_name')
#     office_address = serializers.SerializerMethodField(method_name='get_office_address')
#
#     def get_office_name(self, obj): return str(obj.office)
#
#     def get_office_address(self, obj): return str(obj.office.address)
#
#     class Meta:
#         model = HousingComplex
#         fields = ['id', 'name', 'office', 'office_name', 'office_address']
#
# #####################################################################
#
# class HouseDetSerializer(serializers.ModelSerializer):
#     complex_name = serializers.SerializerMethodField(method_name='get_complex_name')
#     address_str = serializers.SerializerMethodField(method_name='get_address_str')
#     full_name = serializers.SerializerMethodField(method_name='get_full_name')
#
#     def get_complex_name(self, obj): return str(obj.complex)
#
#     def get_address_str(self, obj): return str(obj.address)
#
#     def get_full_name(self, obj): return str(obj)
#
#     class Meta:
#         model = House
#         fields = ['id', 'complex', 'complex_name', 'address', 'address_str', 'full_name']
#
# #####################################################################
#
# class ResidentFullLstMngCrtDelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Resident
#         fields = '__all__'
#
#
# class ResidentFullDetSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField(method_name='get_full_name')
#     respectful_treatment = serializers.SerializerMethodField(method_name='get_respectful_treatment')
#
#     def get_full_name(self, obj): return str(obj)
#
#     def get_respectful_treatment(self, obj): return obj.get_respectful_treatment()
#
#     class Meta:
#         model = Resident
#         fields = ['id', 'name', 'surname', 'patronymic', 'phone', 'tg_id', 'full_name', 'respectful_treatment']
#
#
# class ResidentShortLstSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Resident
#         fields = ['id', 'name', 'surname', 'patronymic']
#
#
# class ResidentShortDetSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField(method_name='get_full_name')
#     respectful_treatment = serializers.SerializerMethodField(method_name='get_respectful_treatment')
#
#     def get_full_name(self, obj): return str(obj)
#
#     def get_respectful_treatment(self, obj): return obj.get_respectful_treatment()
#
#     class Meta:
#         model = Resident
#         fields = ['id', 'name', 'surname', 'patronymic', 'full_name', 'respectful_treatment']
#
# #####################################################################
#
# class ExecutionStatusUltimateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ExecutionStatus
#         fields = '__all__'
#
# #####################################################################
#
# #####################################################################
#
# class PositionDetSerializer(serializers.ModelSerializer):
#     department_name = serializers.SerializerMethodField(method_name='get_department_name')
#
#     def get_department_name(self, obj): return str(obj.department)
#
#     class Meta:
#         model = Position
#         fields = ['id', 'department', 'department_name', 'name']
#
# #####################################################################
#
# class EmployeeFullDetSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField(method_name='get_full_name')
#     respectful_treatment = serializers.SerializerMethodField(method_name='get_respectful_treatment')
#     office_name = serializers.SlugRelatedField(slug_field='name', read_only=True)
#     position_name = serializers.SlugRelatedField(slug_field='name', read_only=True)
#
#     def get_full_name(self, obj): return str(obj)
#
#     def get_respectful_treatment(self, obj): return obj.get_respectful_treatment()
#
#     class Meta:
#         model = Employee
#         fields = ['id', 'name', 'surname', 'patronymic', 'phone', 'email', 'office', 'office_name',
#                   'position', 'position_name', 'tg_id', 'full_name', 'respectful_treatment']
#
#
# class EmployeeShortLstSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['pk', 'name', 'surname', 'patronymic']
#
#
# class EmployeeShortDetSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField(method_name='get_full_name')
#     respectful_treatment = serializers.SerializerMethodField(method_name='get_respectful_treatment')
#
#     def get_full_name(self, obj): return str(obj)
#
#     def get_respectful_treatment(self, obj): return obj.get_respectful_treatment()
#
#     class Meta:
#         model = Employee
#         fields = ['id', 'name', 'surname', 'patronymic', 'email', 'office', 'position', 'full_name',
#                   'respectful_treatment']
#
# #####################################################################
#
# class ServiceDetSerializer(serializers.ModelSerializer):
#     position_name = serializers.SerializerMethodField(method_name='get_position_name')
#
#     def get_position_name(self, obj): return str(obj.position)
#
#     class Meta:
#         model = Service
#         fields = ['id', 'name', 'position', 'position_name', 'description']
#
# #####################################################################


# class RequestDetSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField(method_name='get_full_name')
#
#     def get_full_name(self, obj): return str(obj)
#
#     class Meta:
#         model = Request
#         fields = ['id', 'created_at', 'text', 'status', 'resident', 'address', 'apartment',
#                   'photo', 'employee', 'service', 'full_name']
