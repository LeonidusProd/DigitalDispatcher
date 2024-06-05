# from django.http import HttpResponse
# from django.shortcuts import render
from rest_framework import generics, viewsets
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .permissions import *
from rest_framework import status
import uuid
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser

from .models import *
from django.contrib.auth.models import User
from .serializers import *
from django.db.models import Q

"""
Permissions:
IsSuperuser - Пользователь, который имеет статус супер пользователя
IsStaff - Пользователь, который имеет статус персонала
AllowAny - Любой пользователь
"""


# Используемые
class BuildingListView(generics.ListAPIView):
    """Список всех адресов"""
    queryset = Building.objects.all()
    serializer_class = BuildingLstSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class BuildingCreateView(generics.CreateAPIView):
    """Добавление нового адреса"""
    queryset = Building.objects.all()
    serializer_class = BuildingLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class BuildingDeleteView(generics.DestroyAPIView):
    """Удаление адреса"""
    queryset = Building.objects.all()
    serializer_class = BuildingLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class BotTokensUpdateView(generics.RetrieveUpdateAPIView):
    """Обновление и получение токенов ботов"""
    queryset = BotsSettings.objects.all()
    serializer_class = BotTokensSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class CityListView(generics.ListAPIView):
    """Список всех городов"""
    queryset = City.objects.all()
    serializer_class = CityLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class CityStreetsListView(generics.ListAPIView):
    """Список улиц города"""

    def get_queryset(self):
        return Street.objects.filter(
            city_id=self.kwargs.get('pk')
        )
    serializer_class = StreetLstMngCrtDelSerializer
    permission_classes = (IsSuperuser,)


class CityCreateView(generics.CreateAPIView):
    """Добавление нового города"""
    queryset = City.objects.all()
    serializer_class = CityLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class HousingComplexListView(generics.ListAPIView):
    """Список всех жилых комплексов"""
    queryset = HousingComplex.objects.all()
    serializer_class = HousingComplexLstMngCrtDelSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class HousingComplexCreateView(generics.CreateAPIView):
    """Добавление нового жилого комплекса"""
    queryset = HousingComplex.objects.all()
    serializer_class = HousingComplexLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class HousingComplexDeleteView(generics.DestroyAPIView):
    """Удаление жилого комплекса"""
    queryset = HousingComplex.objects.all()
    serializer_class = HousingComplexLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class HousingComplexHousesListView(generics.ListAPIView):
    """Список домов комплекса"""

    def get_queryset(self):
        return House.objects.filter(
            complex_id=self.kwargs.get('pk')
        )
    serializer_class = HouseShortLstSerializer
    permission_classes = ((IsSuperuser | IsStaff),)


class DepartmentListView(generics.ListAPIView):
    """Список всех отделов"""
    queryset = Department.objects.all()
    serializer_class = DepartmentUltimateSerializer
    permission_classes = (IsSuperuser, )


class DepartmentCreateView(generics.CreateAPIView):
    """Добавление нового отдела"""
    queryset = Department.objects.all()
    serializer_class = DepartmentUltimateSerializer
    permission_classes = (IsSuperuser, )


class DepartmentDeleteView(generics.DestroyAPIView):
    """Удаление отдела"""
    queryset = Department.objects.all()
    serializer_class = DepartmentUltimateSerializer
    permission_classes = (IsSuperuser, )


class EmployeeShortListView(generics.ListAPIView):
    """Список всех сотрудников (без конфиденциальных данных)"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSpecSerializer
    permission_classes = (IsSuperuser, )


class EmployeeCreateView(generics.CreateAPIView):
    """Добавление нового сотрудника"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeFullLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class EmployeeDeleteView(generics.DestroyAPIView):
    """Удаление сотрудника"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeFullLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class HouseListView(generics.ListAPIView):
    """Список всех жилых домов"""
    queryset = House.objects.all()
    serializer_class = HouseLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class HouseCreateView(generics.CreateAPIView):
    """Добавление нового жилого дома"""
    queryset = House.objects.all()
    serializer_class = HouseLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class HouseDeleteView(generics.DestroyAPIView):
    """Удаление жилого дома"""
    queryset = House.objects.all()
    serializer_class = HouseLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class OfficeListView(generics.ListAPIView):
    """Список всех управляющих компаний"""
    queryset = Office.objects.all()
    serializer_class = OfficeLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class OfficeCreateView(generics.CreateAPIView):
    """Добавление новой управляющей компании"""
    queryset = Office.objects.all()
    serializer_class = OfficeLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class OfficeDeleteView(generics.DestroyAPIView):
    """Удаление управляющей компании"""
    queryset = Office.objects.all()
    serializer_class = OfficeLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class PositionListView(generics.ListAPIView):
    """Список всех должностей"""
    queryset = Position.objects.all()
    serializer_class = PositionLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class PositionCreateView(generics.CreateAPIView):
    """Добавление новой должности"""
    queryset = Position.objects.all()
    serializer_class = PositionLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class PositionDeleteView(generics.DestroyAPIView):
    """Удаление должности"""
    queryset = Position.objects.all()
    serializer_class = PositionLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class NewRequestsView(generics.ListAPIView):
    """Список заявок со статусом 'Новая'"""
    queryset = Request.objects.filter(
        status__pk=1
    )
    serializer_class = RequestShortInfoSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class ActiveRequestsView(generics.ListAPIView):
    """Список заявок со статусом 'Новая'"""
    queryset = Request.objects.filter(
        status__pk__in=[2, 3]
    )
    serializer_class = RequestShortInfoSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class RequestDetailView(generics.RetrieveUpdateAPIView):
    """Полная информация о заявке"""
    queryset = Request.objects.all()
    serializer_class = RequestDetSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class RequestTasksView(generics.ListAPIView):
    """Список задач для заявки"""
    def get_queryset(self):
        request_id = self.kwargs.get('pk')
        return RequestTask.objects.filter(
            request_id=request_id
        )
    serializer_class = RequestTaskInfoSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class RequestCreateView(generics.CreateAPIView):
    """Добавление новой заявки"""
    queryset = Request.objects.all()
    serializer_class = RequestLstMngCrtDelSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class RequestCreateByBotView(generics.CreateAPIView):
    """Добавление новой заявки ботом"""
    permission_classes = (IsValidTemporaryToken, )
    serializer_class = RequestLstMngCrtDelSerializer

    def create(self, request, *args, **kwargs):
        token = request.data.get('token')
        temp_token = get_object_or_404(TemporaryToken, token=token)

        # Удаляем токен после использования
        temp_token.delete()

        # Сохранение заявки (данные будут взяты из request.data)
        return super().create(request, *args, **kwargs)


class UserRequestsView(generics.ListAPIView):
    """Список заявок пользователя Tg"""
    def get_queryset(self):
        return Request.objects.filter(
            resident__tg_id=self.kwargs.get('tgID')
        )

    serializer_class = RequestDetSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


#######################################################################
class ResidentListView(generics.ListAPIView):
    """Список всех жителей"""
    queryset = Resident.objects.all()
    serializer_class = ResidentLstSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class ResidentCreateView(generics.CreateAPIView):
    """Добавление нового жителя"""
    queryset = Resident.objects.all()
    serializer_class = ResidentFullLstMngCrtDelSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class ResidentByTgView(APIView):
    permission_classes = ((IsSuperuser | IsStaff), )

    def get(self, request, tgID, format=None):
        try:
            resident = Resident.objects.get(tg_id=tgID)
            serializer = ResidentLstSerializer(resident)
            return Response({'exists': True, 'resident': serializer.data}, status=status.HTTP_200_OK)
        except Resident.DoesNotExist:
            return Response({'exists': False}, status=status.HTTP_404_NOT_FOUND)


class WorkScheduleListView(generics.ListAPIView):
    """Список всех графиков работы"""
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleLstSerializer
    permission_classes = (IsSuperuser, )


class WorkScheduleDetailView(generics.RetrieveAPIView):
    """Полная информация о графике работы"""
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleDetMngSerializer
    permission_classes = (IsSuperuser, )


class WorkDayManageView(generics.RetrieveUpdateAPIView):
    """Изменение информации о рабочем дне"""
    queryset = WorkDay.objects.all()
    serializer_class = WorkDayFullLstSerializer
    permission_classes = (IsSuperuser, )


class WorkScheduleCreateView(generics.CreateAPIView):
    """Добавление нового графика работы"""
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleCrtDelSerializer
    permission_classes = (IsSuperuser, )


class WorkScheduleDeleteView(generics.DestroyAPIView):
    """Удаление графика работы"""
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleCrtDelSerializer
    permission_classes = (IsSuperuser, )


class StreetCreateView(generics.CreateAPIView):
    """Добавление новой улицы"""
    queryset = Street.objects.all()
    serializer_class = StreetLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class ServiceListView(generics.ListAPIView):
    """Список всех типовых задач"""
    queryset = Service.objects.all()
    serializer_class = ServiceLstMngCrtDelSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class ServiceEmployeesView(generics.ListAPIView):
    """Список сотрудников, подходящих для задачи"""
    def get_queryset(self):
        data = self.request.query_params
        print(data)
        return Employee.objects.filter(
            position_id=data.get('position_pk'),
            office_id=data.get('office_pk')
        )
    serializer_class = ServiseEmployeesSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class ServiceCreateView(generics.CreateAPIView):
    """Добавление новой типовой задачи"""
    queryset = Service.objects.all()
    serializer_class = ServiceLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class ServiceDeleteView(generics.DestroyAPIView):
    """Удаление типовой задачи"""
    queryset = Service.objects.all()
    serializer_class = ServiceLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class TaskFullInfoView(generics.RetrieveUpdateAPIView):
    """Список всех типовых задач"""
    queryset = RequestTask.objects.all()
    serializer_class = TaskFullInfoSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class TaskCreateView(generics.CreateAPIView):
    """Создание задачи заявки"""
    queryset = RequestTask.objects.all()
    serializer_class = RequestTaskDelSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class TaskDeleteView(generics.DestroyAPIView):
    """Удаление задачи заявки"""
    queryset = RequestTask.objects.all()
    serializer_class = RequestTaskDelSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class TasksForMasterView(generics.ListAPIView):
    """Список задач пользователя Tg"""
    def get_queryset(self):
        return RequestTask.objects.filter(
            employee__tg_id=self.kwargs.get('tgID'),
            status__in=[1, 2, 3]
        )

    serializer_class = RequestTaskInfoSerializer
    permission_classes = ((IsSuperuser | IsStaff), )


class UserListView(generics.ListAPIView):
    """Список всех пользователей"""
    queryset = User.objects.filter(~Q(pk=1))
    serializer_class = UserLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class UserCreateView(generics.CreateAPIView):
    """Добавление нового пользователя"""
    queryset = User.objects.all()
    serializer_class = UserLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


class UserDeleteView(generics.DestroyAPIView):
    """Удаление пользователя"""
    queryset = User.objects.all()
    serializer_class = UserLstMngCrtDelSerializer
    permission_classes = (IsSuperuser, )


# Специализированные view
class GenerateTempTokenView(generics.CreateAPIView):
    queryset = TemporaryToken.objects.all()
    serializer_class = TemporaryTokenSerializer
    permission_classes = ((IsSuperuser | IsStaff), )

    def create(self, request, *args, **kwargs):
        token = str(uuid.uuid4())
        created_to = request.data.get('created_to')
        temp_token = TemporaryToken.objects.create(token=token, created_to=created_to)
        return Response({'token': temp_token.token})


# Не используются в настоящий момент
# class CityDetailView(generics.RetrieveAPIView):
#     """Полная информация о городе"""
#     queryset = City.objects.all()
#     serializer_class = CityDetSerializer
#     permission_classes = (AllowAny, )
#
#
# class CityManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации о городе"""
#     queryset = City.objects.all()
#     serializer_class = CityLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
#
# class CityDeleteView(generics.DestroyAPIView):
#     """Удаление города"""
#     queryset = City.objects.all()
#     serializer_class = CityLstMngCrtDelSerializer
#     permission_classes = (AllowAny, )
#
# #####################################################################
#
# class StreetListView(generics.ListAPIView):
#     """Список всех улиц"""
#     queryset = Street.objects.all()
#     serializer_class = StreetLstMngCrtDelSerializer
#     permission_classes = (AllowAny, )
#
#
# class StreetDetailView(generics.RetrieveAPIView):
#     """Полная информация об улице"""
#     queryset = Street.objects.all()
#     serializer_class = StreetDetSerializer
#     permission_classes = (AllowAny, )
#
#
# class StreetManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации об улице"""
#     queryset = Street.objects.all()
#     serializer_class = StreetLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
#
# class StreetDeleteView(generics.DestroyAPIView):
#     """Удаление улицы"""
#     queryset = Street.objects.all()
#     serializer_class = StreetLstMngCrtDelSerializer
#     permission_classes = (AllowAny, )
#
# #####################################################################
#
# class BuildingDetailView(generics.RetrieveAPIView):
#     """Полная информация об адресе"""
#     queryset = Building.objects.all()
#     serializer_class = BuildingDetSerializer
#     permission_classes = (AllowAny, )
#
#
# class BuildingManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации об адресе"""
#     queryset = Building.objects.all()
#     serializer_class = BuildingLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
# #####################################################################
#
# class WorkScheduleManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации о графике работы """
#     queryset = WorkSchedule.objects.all()
#     serializer_class = WorkScheduleDetMngSerializer
#     permission_classes = (AllowAny, )
#
# #####################################################################
#
# class OfficeDetailView(generics.RetrieveAPIView):
#     """Полная информация об управляющей компании"""
#     queryset = Office.objects.all()
#     serializer_class = OfficeDetSerializer
#     permission_classes = (AllowAny, )
#
#
# class OfficeManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации об управляющей компании"""
#     queryset = Office.objects.all()
#     serializer_class = OfficeLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
# #####################################################################
#
# class HousingComplexDetailView(generics.RetrieveAPIView):
#     """Полная информация о жилом комплексе"""
#     queryset = HousingComplex.objects.all()
#     serializer_class = HousingComplexDetSerializer
#     permission_classes = (AllowAny, )
#
#
# class HousingComplexManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации о жилом комплексе"""
#     queryset = HousingComplex.objects.all()
#     serializer_class = HousingComplexLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
# #####################################################################
#
# class HouseDetailView(generics.RetrieveAPIView):
#     """Полная информация о жилом доме"""
#     queryset = House.objects.all()
#     serializer_class = HouseDetSerializer
#     permission_classes = (AllowAny, )
#
#
# class HouseManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации о жилом доме"""
#     queryset = House.objects.all()
#     serializer_class = HouseLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
# #####################################################################
#
# class ResidentShortListView(generics.ListAPIView):
#     """Список всех жителей (без конфиденциальных данных)"""
#     queryset = Resident.objects.all()
#     serializer_class = ResidentShortLstSerializer
#     permission_classes = (AllowAny, )
#
#
# class ResidentShortDetailView(generics.RetrieveAPIView):
#     """Полная информация о жителе (без конфиденциальных данных)"""
#     queryset = Resident.objects.all()
#     serializer_class = ResidentShortDetSerializer
#     permission_classes = (AllowAny, )
#
#
# class ResidentFullListView(generics.ListAPIView):
#     """Список всех жителей (с конфиденциальными данными)"""
#     queryset = Resident.objects.all()
#     serializer_class = ResidentFullLstMngCrtDelSerializer
#     permission_classes = (IsStaff, )
#
#
# class ResidentFullDetailView(generics.RetrieveAPIView):
#     """Полная информация о жителе (с конфиденциальными данными)"""
#     queryset = Resident.objects.all()
#     serializer_class = ResidentFullDetSerializer
#     permission_classes = (IsStaff, )
#
#
# class ResidentManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации о жителе"""
#     queryset = Resident.objects.all()
#     serializer_class = ResidentFullLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
#
# class ResidentDeleteView(generics.DestroyAPIView):
#     """Удаление жителя"""
#     queryset = Resident.objects.all()
#     serializer_class = ResidentFullLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
# #####################################################################
#
# class ExecutionStatusListView(generics.ListAPIView):
#     """Список всех статусов выполнения"""
#     queryset = ExecutionStatus.objects.all()
#     serializer_class = ExecutionStatusUltimateSerializer
#     permission_classes = (AllowAny, )
#
#
# class ExecutionStatusDetailView(generics.RetrieveAPIView):
#     """Полная информация о статусе выполнения"""
#     queryset = ExecutionStatus.objects.all()
#     serializer_class = ExecutionStatusUltimateSerializer
#     permission_classes = (AllowAny, )
#
#
# class ExecutionStatusManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации о статусе выполнения"""
#     queryset = ExecutionStatus.objects.all()
#     serializer_class = ExecutionStatusUltimateSerializer
#     permission_classes = (IsSuperuser, )
#
#
# class ExecutionStatusCreateView(generics.CreateAPIView):
#     """Добавление нового статуса выполнения"""
#     queryset = ExecutionStatus.objects.all()
#     serializer_class = ExecutionStatusUltimateSerializer
#     permission_classes = (IsSuperuser, IsStaff, )
#
#
# class ExecutionStatusDeleteView(generics.DestroyAPIView):
#     """Удаление статуса выполнения"""
#     queryset = ExecutionStatus.objects.all()
#     serializer_class = ExecutionStatusUltimateSerializer
#     permission_classes = (IsSuperuser, )
#
# #####################################################################
#
# class DepartmentDetailView(generics.RetrieveAPIView):
#     """Полная информация об отделе"""
#     queryset = Department.objects.all()
#     serializer_class = DepartmentUltimateSerializer
#     permission_classes = (AllowAny, )
#
#
# class DepartmentManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации об отделе"""
#     queryset = Department.objects.all()
#     serializer_class = DepartmentUltimateSerializer
#     permission_classes = (IsSuperuser, )
#
# #####################################################################
#
# class PositionDetailView(generics.RetrieveAPIView):
#     """Полная информация о должности"""
#     queryset = Position.objects.all()
#     serializer_class = PositionDetSerializer
#     permission_classes = (AllowAny, )
#
#
# class PositionManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации о должности"""
#     queryset = Position.objects.all()
#     serializer_class = PositionLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
# #####################################################################
#
# class EmployeeShortDetailView(generics.RetrieveAPIView):
#     """Полная информация о сотруднике (без конфиденциальных данных)"""
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeShortDetSerializer
#     permission_classes = (AllowAny, )
#
#
# class EmployeeFullListView(generics.ListAPIView):
#     """Список всех сотрудников (с конфиденциальными данными)"""
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeFullLstMngCrtDelSerializer
#     permission_classes = (IsStaff, )
#
#
# class EmployeeFullDetailView(generics.RetrieveAPIView):
#     """Полная информация о сотруднике (с конфиденциальными данными)"""
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeFullDetSerializer
#     permission_classes = (IsStaff, )
#
#
# class EmployeeManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации о сотруднике"""
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeFullLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
# #####################################################################
#
# class ServiceDetailView(generics.RetrieveAPIView):
#     """Полная информация о типовой задаче"""
#     queryset = Service.objects.all()
#     serializer_class = ServiceDetSerializer
#     permission_classes = (AllowAny, )
#
#
# class ServiceManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации о типовой задаче"""
#     queryset = Service.objects.all()
#     serializer_class = ServiceLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
# #####################################################################
#
# class RequestListView(generics.ListAPIView):
#     """Список всех заявок"""
#     queryset = Request.objects.all()
#     serializer_class = RequestLstMngCrtDelSerializer
#     permission_classes = (AllowAny, )
#
#
# class RequestManageView(generics.RetrieveUpdateAPIView):
#     """Изменение информации о заявке"""
#     queryset = Request.objects.all()
#     serializer_class = RequestLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
#
# class RequestDeleteView(generics.DestroyAPIView):
#     """Удаление заявки"""
#     queryset = Request.objects.all()
#     serializer_class = RequestLstMngCrtDelSerializer
#     permission_classes = (IsSuperuser, )
#
#
# class TestView(APIView):
#     def get(self, request):
#         return Response(
#             {
#                 'test_data': 'This is test data'
#             }
#         )
#
#
# class BotTokensView(generics.ListAPIView):
#     """Токены ботов"""
#     queryset = BotsSettings.objects.all()
#     serializer_class = BotTokensSerializer
#     permission_classes = (AllowAny, )
#

# class ComplexList(ListAPIView):
#     queryset = HousingComplex.objects.all()
#     serializer_class = HousingComplexSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#
#
# class HouseList(ListAPIView):
#     queryset = House.objects.all()
#     serializer_class = HouseSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#
#
# class ComplexHousesList(APIView):
#     def get(self, request, complex_id):
#         houses = House.objects.filter(complex_id=complex_id)
#
#         data = []
#         for house in houses:
#             data.append(
#                 {
#                     'pk': house.pk,
#                     'complex': house.complex.name,
#                     'address': house.address.short_str()
#                 }
#             )
#
#         return Response(
#             data
#         )
#
#
# class ResidentByTg(APIView):
#     def get(self, request, user_tgID):
#         resident = Resident.objects.filter(tg_id=user_tgID)
#
#         data = []
#
#         if not resident:
#             data.append({
#                 'is_exist': False
#             })
#         else:
#             data.append({
#                 'is_exist': True,
#                 'pk': resident.pk
#             })
#
#         return Response(
#             data
#         )
#
#
# class ResidentList(APIView):
#     def get(self):
#         pass
#
#     def post(self, request):
#         data = request.data
#         snp = data['snp'].split(' ')
#         surname = snp[0]
#         try:
#             name = snp[1]
#         except IndexError:
#             name = ''
#         try:
#             patronymic = snp[2]
#         except IndexError:
#             patronymic = ''
#         phone = data['phone']
#         tg_id = data['tg_id']
#
#         new_resident = Resident(
#             name=name,
#             surname=surname,
#             patronymic=patronymic,
#             phone=phone,
#             tg_id=tg_id
#         )
#         new_resident.save()
#
#         return Response(
#             {
#                 'success': True,
#                 'resident_id': new_resident.pk
#             }
#         )
#
#
# class RequestList(APIView):
#     def post(self, request):
#         data = request.data
#         text = data['text']
#         status = ExecutionStatus.objects.get(pk=1)
#         resident = Resident.objects.get(pk=data['resident'])
#         address = House.objects.get(pk=data['house'])
#         apartment = data['apartment'] if 'apartment' in data else '-'
#         photo = data['photo'] if 'photo' in data else ''
#
#         new_request = Request(
#             text=text,
#             status=status,
#             resident=resident,
#             address=address,
#             photo=photo,
#             apartment=apartment
#         )
#         new_request.save()
#
#         return Response(
#             {
#                 'success': True,
#                 'new_request_id': new_request.pk
#             }
#         )
