from rest_framework import generics
from rest_framework.views import APIView

from .permissions import *
from rest_framework import status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, inline_serializer, OpenApiExample

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
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Список всех адресов",
        description="Получение списка всех адресов в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["address"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BuildingCreateView(generics.CreateAPIView):
    """Добавление нового адреса"""
    queryset = Building.objects.all()
    serializer_class = BuildingCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Добавление нового адреса",
        description="Добавление нового адреса в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["address"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class BuildingDeleteView(generics.DestroyAPIView):
    """Удаление адреса"""
    queryset = Building.objects.all()
    serializer_class = BuildingCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Удаление адреса",
        description="Удаление адреса из системы.",
        responses={
            status.HTTP_204_NO_CONTENT: inline_serializer(
                name="NoContentResponse",
                fields={"detail": serializers.CharField(default="Адрес удалён")}
            ),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["address"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class BotTokensUpdateView(generics.RetrieveUpdateAPIView):
    """Обновление и получение токенов ботов"""
    queryset = BotsSettings.objects.all()
    serializer_class = BotTokensSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Получение токенов ботов",
        description="Получение токенов ботов, предполагаемых к использованию.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["bot-tokens"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Обновление токенов ботов",
        description="Обновление токенов ботов, предполагаемых к использованию.",
        request=serializer_class,
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["bot-tokens"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Обновление токенов ботов",
        description="Обновление токенов ботов, предполагаемых к использованию.",
        request=serializer_class,
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["bot-tokens"]
    )
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class CityListView(generics.ListAPIView):
    """Список всех городов"""
    queryset = City.objects.all()
    serializer_class = CityLstCrtSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Список всех городов",
        description="Получение списка всех городов в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["city"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CityStreetsListView(generics.ListAPIView):
    """Список улиц города"""

    def get_queryset(self):
        return Street.objects.filter(
            city_id=self.kwargs.get('pk')
        )

    serializer_class = StreetLstCrtSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Список всех улиц города",
        description="Получение списка всех улиц города в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["city"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CityCreateView(generics.CreateAPIView):
    """Добавление нового города"""
    queryset = City.objects.all()
    serializer_class = CityLstCrtSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Добавление нового города",
        description="Добавление нового города в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["city"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class HousingComplexListView(generics.ListAPIView):
    """Список всех жилых комплексов"""
    queryset = HousingComplex.objects.all()
    serializer_class = HousingComplexLstCrtDelSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Список всех жилых комплексов",
        description="Получение списка всех жилых комплексов в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["complex"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class HousingComplexCreateView(generics.CreateAPIView):
    """Добавление нового жилого комплекса"""
    queryset = HousingComplex.objects.all()
    serializer_class = HousingComplexLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Добавление нового жилого комплекса",
        description="Добавление нового жилого комплекса в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["complex"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class HousingComplexDeleteView(generics.DestroyAPIView):
    """Удаление жилого комплекса"""
    queryset = HousingComplex.objects.all()
    serializer_class = HousingComplexLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Удаление жилого комплекса",
        description="Удаление жилого комплекса из системы.",
        responses={
            status.HTTP_204_NO_CONTENT: inline_serializer(
                name="NoContentResponse",
                fields={"detail": serializers.CharField(default="Комплекс удалён")}
            ),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["complex"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class HousingComplexHousesListView(generics.ListAPIView):
    """Список домов комплекса"""

    serializer_class = ComplexHousesLstSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    def get_queryset(self):
        return House.objects.filter(
            complex_id=self.kwargs.get('pk')
        )

    @extend_schema(
        summary="Список всех домов жилого комплекса",
        description="Получение списка всех домов жилого комплекса.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["complex"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class DepartmentListView(generics.ListAPIView):
    """Список всех отделов"""
    queryset = Department.objects.all()
    serializer_class = DepartmentLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Список всех отделов",
        description="Получение списка всех отделов в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["department"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class DepartmentCreateView(generics.CreateAPIView):
    """Добавление нового отдела"""
    queryset = Department.objects.all()
    serializer_class = DepartmentLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Добавление нового отдела",
        description="Добавление нового отдела в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["department"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DepartmentDeleteView(generics.DestroyAPIView):
    """Удаление отдела"""
    queryset = Department.objects.all()
    serializer_class = DepartmentLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Удаление отдела",
        description="Удаление отдела из системы.",
        responses={
            status.HTTP_204_NO_CONTENT: inline_serializer(
                name="NoContentResponse",
                fields={"detail": serializers.CharField(default="Отдел удалён")}
            ),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["department"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class EmployeeShortListView(generics.ListAPIView):
    """Список всех сотрудников"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeLstSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Список всех сотрудников",
        description="Получение списка всех сотрудников в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["employee"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class EmployeeCreateView(generics.CreateAPIView):
    """Добавление нового сотрудника"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Добавление нового сотрудника",
        description="Добавление нового сотрудника в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["employee"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class EmployeeDeleteView(generics.DestroyAPIView):
    """Удаление сотрудника"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Удаление сотрудника",
        description="Удаление сотрудника из системы.",
        responses={
            status.HTTP_204_NO_CONTENT: inline_serializer(
                name="NoContentResponse",
                fields={"detail": serializers.CharField(default="Сотрудник удалён")}
            ),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["employee"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class HouseListView(generics.ListAPIView):
    """Список всех жилых домов"""
    queryset = House.objects.all()
    serializer_class = HouseLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Список всех жилых домов",
        description="Получение списка всех жилых домов в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["house"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class HouseCreateView(generics.CreateAPIView):
    """Добавление нового жилого дома"""
    queryset = House.objects.all()
    serializer_class = HouseLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Добавление нового жилого дома",
        description="Добавление нового жилого дома в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["house"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class HouseDeleteView(generics.DestroyAPIView):
    """Удаление жилого дома"""
    queryset = House.objects.all()
    serializer_class = HouseLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Удаление жилого дома",
        description="Удаление жилого дома из системы.",
        responses={
            status.HTTP_204_NO_CONTENT: inline_serializer(
                name="NoContentResponse",
                fields={"detail": serializers.CharField(default="Жилой дом удалён")}
            ),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["house"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class OfficeListView(generics.ListAPIView):
    """Список всех управляющих компаний"""
    queryset = Office.objects.all()
    serializer_class = OfficeLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Список всех управляющих компаний",
        description="Получение списка всех управляющих компаний в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["office"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class OfficeCreateView(generics.CreateAPIView):
    """Добавление новой управляющей компании"""
    queryset = Office.objects.all()
    serializer_class = OfficeLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Добавление новой управляющей компании",
        description="Добавление новой управляющей компании в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["office"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class OfficeDeleteView(generics.DestroyAPIView):
    """Удаление управляющей компании"""
    queryset = Office.objects.all()
    serializer_class = OfficeLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Удаление управляющей компании",
        description="Удаление управляющей компании из системы.",
        responses={
            status.HTTP_204_NO_CONTENT: inline_serializer(
                name="NoContentResponse",
                fields={"detail": serializers.CharField(default="Управляющая компания удалена")}
            ),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["office"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class PositionListView(generics.ListAPIView):
    """Список всех должностей"""
    queryset = Position.objects.all()
    serializer_class = PositionLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Список всех должностей",
        description="Получение списка всех должностей в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["position"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PositionCreateView(generics.CreateAPIView):
    """Добавление новой должности"""
    queryset = Position.objects.all()
    serializer_class = PositionLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Добавление новой должности",
        description="Добавление новой должности в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["position"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class PositionDeleteView(generics.DestroyAPIView):
    """Удаление должности"""
    queryset = Position.objects.all()
    serializer_class = PositionLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Удаление должности",
        description="Удаление должности из системы.",
        responses={
            status.HTTP_204_NO_CONTENT: inline_serializer(
                name="NoContentResponse",
                fields={"detail": serializers.CharField(default="Должность удалена")}
            ),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["position"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class NewRequestsView(generics.ListAPIView):
    """Список заявок со статусом 'Новая'"""
    queryset = Request.objects.filter(
        status__pk=1
    )
    serializer_class = RequestShortInfoSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Список всех заявок со статусом 'Новая'",
        description="Получение списка всех заявок со статусом 'Новая' в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ActiveRequestsView(generics.ListAPIView):
    """Список заявок со статусом, относящимся к активным"""
    queryset = Request.objects.filter(
        status__pk__in=[2, 3]
    )
    serializer_class = RequestShortInfoSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Список всех заявок со статусом, относящимся к активным",
        description="Получение списка всех заявок со статусом, относящимся к активным в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class RequestDetailView(generics.RetrieveUpdateAPIView):
    """Полная информация о заявке"""
    queryset = Request.objects.all()
    serializer_class = RequestDetSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Получение полной информации о заявке",
        description="Получение полной информации о заявке.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Обновление информации о заявке",
        description="Обновление информации о заявке.",
        request=serializer_class,
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Обновление информации о заявке",
        description="Обновление информации о заявке.",
        request=serializer_class,
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request"]
    )
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class RequestTasksView(generics.ListAPIView):
    """Список задач для заявки"""

    serializer_class = RequestTaskInfoSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    def get_queryset(self):
        request_id = self.kwargs.get('pk')
        return RequestTask.objects.filter(
            request_id=request_id
        )

    @extend_schema(
        summary="Список задач для заявки",
        description="Получение списка задач для конкретной заявки.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class RequestCreateView(generics.CreateAPIView):
    """Добавление новой заявки"""
    queryset = Request.objects.all()
    serializer_class = RequestCrtSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Добавление новой заявки",
        description="Добавление новой заявки в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserRequestsView(generics.ListAPIView):
    """Список заявок пользователя Tg"""

    serializer_class = RequestDetSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    def get_queryset(self):
        return Request.objects.filter(
            resident__tg_id=self.kwargs.get('tgID')
        )

    @extend_schema(
        summary="Список заявок пользователя Tg",
        description="Получение списка заявок у конкретного пользователя Tg по его user_id.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ResidentListView(generics.ListAPIView):
    """Список всех жителей"""
    queryset = Resident.objects.all()
    serializer_class = ResidentLstSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Список жителей",
        description="Получение списка жителей.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["resident"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ResidentCreateView(generics.CreateAPIView):
    """Добавление нового жителя"""
    queryset = Resident.objects.all()
    serializer_class = ResidentCrtSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Добавление нового жителя",
        description="Добавление нового жителя в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["resident"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ResidentByTgView(APIView):
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Получение жителя по tgID (Tg user_id)",
        description="Проверяет наличие жителя в базе данных на основе переданного tgID и "
                    "возвращает его данные при существовании.",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="ResidentResponse",
                fields={
                    'exists': serializers.BooleanField(),
                    'resident': ResidentLstSerializer()
                }
            ),
            status.HTTP_404_NOT_FOUND: inline_serializer(
                name="NotFoundResponse",
                fields={'exists': serializers.BooleanField(default=False)}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["resident"]
    )
    def get(self, request, tgID):
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
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Список графиков работы",
        description="Получение списка графиков работы.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["schedule"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class WorkScheduleDetailView(generics.RetrieveAPIView):
    """Полная информация о графике работы"""
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleDetMngSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Получение полной информации о графике работы",
        description="Получение полной информации о графике работы.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["schedule"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class WorkDayManageView(generics.RetrieveUpdateAPIView):
    """Изменение информации о рабочем дне"""
    queryset = WorkDay.objects.all()
    serializer_class = WorkDayFullLstSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Получение полной информации о рабочем дне",
        description="Получение полной информации о рабочем дне.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["schedule"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Обновление информации о рабочем дне",
        description="Обновление информации о рабочем дне.",
        request=serializer_class,
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["schedule"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Обновление информации о рабочем дне",
        description="Обновление информации о рабочем дне.",
        request=serializer_class,
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["schedule"]
    )
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class WorkScheduleCreateView(generics.CreateAPIView):
    """Добавление нового графика работы"""
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Добавление нового графика работы",
        description="Добавление нового графика работы в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["schedule"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class WorkScheduleDeleteView(generics.DestroyAPIView):
    """Удаление графика работы"""
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Удаление графика работы",
        description="Удаление графика работы из системы.",
        responses={
            status.HTTP_204_NO_CONTENT: inline_serializer(
                name="NoContentResponse",
                fields={"detail": serializers.CharField(default="График работы удалён")}
            ),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["schedule"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class StreetCreateView(generics.CreateAPIView):
    """Добавление новой улицы"""
    queryset = Street.objects.all()
    serializer_class = StreetLstCrtSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Добавление новой улицы",
        description="Добавление новой улицы в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["street"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ServiceListView(generics.ListAPIView):
    """Список всех типовых задач"""

    queryset = Service.objects.all()
    serializer_class = ServiceLstCrtDelSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Список типовых задач",
        description="Получение списка типовых задач.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["service"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ServiceEmployeesView(generics.ListAPIView):
    """Список сотрудников, подходящих для задачи"""

    serializer_class = ServiseEmployeesSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    def get_queryset(self):
        data = self.request.query_params
        print(data)
        return Employee.objects.filter(
            position_id=data.get('position_pk'),
            office_id=data.get('office_pk')
        )

    @extend_schema(
        summary="Список сотрудников, подходящих для задачи",
        description="Получение списка сотрудников, подходящих для задачи.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["service"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ServiceCreateView(generics.CreateAPIView):
    """Добавление новой типовой задачи"""
    queryset = Service.objects.all()
    serializer_class = ServiceLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Добавление новой типовой задачи",
        description="Добавление новой типовой задачи в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["service"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ServiceDeleteView(generics.DestroyAPIView):
    """Удаление типовой задачи"""
    queryset = Service.objects.all()
    serializer_class = ServiceLstCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Удаление типовой задачи",
        description="Удаление типовой задачи из системы.",
        responses={
            status.HTTP_204_NO_CONTENT: inline_serializer(
                name="NoContentResponse",
                fields={"detail": serializers.CharField(default="Типовая задача удалена")}
            ),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["service"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class TaskFullInfoView(generics.RetrieveUpdateAPIView):
    """Получение задачи для заявки"""
    queryset = RequestTask.objects.all()
    serializer_class = TaskFullInfoSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Получение полной информации о задаче для заявки",
        description="Получение полной информации о конкретной задаче для конкретной заявки.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request-task"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Обновление информации о задаче для заявки",
        description="Обновление информации о конкретной задаче для конкретной заявки.",
        request=serializer_class,
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request-task"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Обновление информации о задаче для заявки",
        description="Обновление информации о конкретной задаче для конкретной заявки.",
        request=serializer_class,
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request-task"]
    )
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class TaskCreateView(generics.CreateAPIView):
    """Создание задачи заявки"""
    queryset = RequestTask.objects.all()
    serializer_class = RequestTaskDelSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Добавление новой задачи заявки",
        description="Добавление новой задачи для заявки в системе.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request-task"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TaskDeleteView(generics.DestroyAPIView):
    """Удаление задачи заявки"""
    queryset = RequestTask.objects.all()
    serializer_class = RequestTaskDelSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    @extend_schema(
        summary="Удаление задачи заявки",
        description="Удаление задачи заявки из системы.",
        responses={
            status.HTTP_204_NO_CONTENT: inline_serializer(
                name="NoContentResponse",
                fields={"detail": serializers.CharField(default="Задача заявки удалена")}
            ),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request-task"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class TasksForMasterView(generics.ListAPIView):
    """Список задач пользователя Tg"""

    serializer_class = RequestTaskInfoSerializer
    permission_classes = ((IsSuperuser | IsStaff),)

    def get_queryset(self):
        return RequestTask.objects.filter(
            employee__tg_id=self.kwargs.get('tgID'),
            status__in=[1, 2, 3]
        )

    @extend_schema(
        summary="Список задач пользователя по tgID (Tg user_id)",
        description="Получение списка задач пользователя по tgID (Tg user_id).",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["request-task"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserListView(generics.ListAPIView):
    """Список всех пользователей"""
    queryset = User.objects.filter(~Q(pk=1))
    serializer_class = UserLstMngCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Список всех пользователей",
        description="Получение списка всех пользователей, кроме пользователя c pk=1.",
        responses={
            status.HTTP_200_OK: serializer_class(many=True),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='BadRequest',
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["user"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserCreateView(generics.CreateAPIView):
    """Добавление нового пользователя"""
    queryset = User.objects.all()
    serializer_class = UserLstMngCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Добавление нового пользователя",
        description="Добавление нового пользователя.",
        responses={
            status.HTTP_200_OK: serializer_class(),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["user"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserDeleteView(generics.DestroyAPIView):
    """Удаление пользователя"""
    queryset = User.objects.all()
    serializer_class = UserLstMngCrtDelSerializer
    permission_classes = (IsSuperuser,)

    @extend_schema(
        summary="Удаление пользователя",
        description="Удаление пользователя из системы.",
        responses={
            status.HTTP_204_NO_CONTENT: inline_serializer(
                name="NoContentResponse",
                fields={"detail": serializers.CharField(default="Пользователь удалён")}
            ),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="BadRequestResponse",
                fields={"detail": serializers.CharField(default="Неверный запрос")}
            ),
            status.HTTP_401_UNAUTHORIZED: inline_serializer(
                name="UnauthorizedResponse",
                fields={"detail": serializers.CharField(default="Неавторизованный доступ")}
            ),
            status.HTTP_403_FORBIDDEN: inline_serializer(
                name="ForbiddenResponse",
                fields={"detail": serializers.CharField(default="Доступ запрещен")}
            ),
        },
        tags=["user"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
