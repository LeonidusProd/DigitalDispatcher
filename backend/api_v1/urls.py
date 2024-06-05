from django.urls import path, include

from . import views

urlpatterns = [
    # Используемые
    path('address/', views.BuildingListView.as_view(), name='address_list'),
    path('address/create/', views.BuildingCreateView.as_view(), name='address_create'),
    path('address/delete/<int:pk>', views.BuildingDeleteView.as_view(), name='address_delete'),

    path('bottokens/manage/<int:pk>', views.BotTokensUpdateView.as_view(), name='bottokens_manage'),

    path('city/', views.CityListView.as_view(), name='city_list'),
    path('city/<int:pk>/streets', views.CityStreetsListView.as_view(), name='city_streets_list'),
    path('city/create/', views.CityCreateView.as_view(), name='city_create'),

    path('complex/', views.HousingComplexListView.as_view(), name='complex_list'),
    path('complex/create/', views.HousingComplexCreateView.as_view(), name='complex_create'),
    path('complex/delete/<int:pk>', views.HousingComplexDeleteView.as_view(), name='complex_delete'),
    path('complex/<int:pk>/houses', views.HousingComplexHousesListView.as_view(), name='complex_houses_list'),

    path('department/', views.DepartmentListView.as_view(), name='department_list'),
    path('department/create/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('department/delete/<int:pk>', views.DepartmentDeleteView.as_view(), name='department_delete'),

    path('employee/', views.EmployeeShortListView.as_view(), name='employee_list'),
    path('employee/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/delete/<int:pk>', views.EmployeeDeleteView.as_view(), name='employee_delete'),

    path('house/', views.HouseListView.as_view(), name='house_list'),
    path('house/create/', views.HouseCreateView.as_view(), name='house_create'),
    path('house/delete/<int:pk>', views.HouseDeleteView.as_view(), name='house_delete'),

    path('office/', views.OfficeListView.as_view(), name='office_list'),
    path('office/create/', views.OfficeCreateView.as_view(), name='office_create'),
    path('office/delete/<int:pk>', views.OfficeDeleteView.as_view(), name='office_delete'),

    path('position/', views.PositionListView.as_view(), name='position_list'),
    path('position/create/', views.PositionCreateView.as_view(), name='position_create'),
    path('position/delete/<int:pk>', views.PositionDeleteView.as_view(), name='position_delete'),

    path('requests/new', views.NewRequestsView.as_view(), name='new_requests'),
    path('requests/active', views.ActiveRequestsView.as_view(), name='active_requests'),
    path('request/<int:pk>', views.RequestDetailView.as_view(), name='request_detail'),
    path('request/<int:pk>/tasks', views.RequestTasksView.as_view(), name='request_tasks'),
    path('request/create/', views.RequestCreateView.as_view(), name='request_create'),
    path('request/create/by-bot', views.RequestCreateByBotView.as_view(), name='request_create_by_bot'),
    path('requests/from-user/<int:tgID>', views.UserRequestsView.as_view(), name='new_requests'),

    path('resident/', views.ResidentListView.as_view(), name='resident_list'),
    path('resident/create/', views.ResidentCreateView.as_view(), name='resident_create'),
    path('resident/by_tgid/<int:tgID>', views.ResidentByTgView.as_view(), name='resident_byTG'),

    path('schedule/', views.WorkScheduleListView.as_view(), name='schedule_list'),
    path('schedule/<int:pk>', views.WorkScheduleDetailView.as_view(), name='schedule_detail'),
    path('schedule/workday/manage/<int:pk>', views.WorkDayManageView.as_view(), name='workday_manage'),
    path('schedule/create/', views.WorkScheduleCreateView.as_view(), name='schedule_create'),
    path('schedule/delete/<int:pk>', views.WorkScheduleDeleteView.as_view(), name='schedule_delete'),

    path('street/create/', views.StreetCreateView.as_view(), name='street_create'),

    path('service/', views.ServiceListView.as_view(), name='service_list'),
    path('service/employees/', views.ServiceEmployeesView.as_view(), name='service_employees_list'),
    path('service/create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('service/delete/<int:pk>', views.ServiceDeleteView.as_view(), name='service_delete'),

    path('task/<int:pk>', views.TaskFullInfoView.as_view(), name='create_full_info'),
    path('task/create', views.TaskCreateView.as_view(), name='create_task'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name='delete_task'),
    path('tasks/for-master/<int:tgID>', views.TasksForMasterView.as_view(), name='tasks_for_master'),

    path('user/', views.UserListView.as_view(), name='user_list'),
    path('user/create/', views.UserCreateView.as_view(), name='user_create'),
    path('user/delete/<int:pk>', views.UserDeleteView.as_view(), name='user_delete'),

    # Специализированные api
    path('generate-add-request-token', views.GenerateTempTokenView.as_view())

    # Не используются в настоящий момент
    # path('city/<int:pk>', views.CityDetailView.as_view(), name='city_detail'),
    # path('city/manage/<int:pk>', views.CityManageView.as_view(), name='city_manage'),
    # path('city/delete/<int:pk>', views.CityDeleteView.as_view(), name='city_delete'),
    # path('street/', views.StreetListView.as_view(), name='street_list'),
    # path('street/<int:pk>', views.StreetDetailView.as_view(), name='street_detail'),
    # path('street/manage/<int:pk>', views.StreetManageView.as_view(), name='street_manage'),
    # path('street/delete/<int:pk>', views.StreetDeleteView.as_view(), name='street_delete'),
    # path('address/<int:pk>', views.BuildingDetailView.as_view(), name='address_detail'),
    # path('address/manage/<int:pk>', views.BuildingManageView.as_view(), name='address_manage'),
    # path('schedule/manage/<int:pk>', views.WorkScheduleManageView.as_view(), name='schedule_manage'),
    # path('office/<int:pk>', views.OfficeDetailView.as_view(), name='office_detail'),
    # path('office/manage/<int:pk>', views.OfficeManageView.as_view(), name='office_manage'),
    # path('complex/<int:pk>', views.HousingComplexDetailView.as_view(), name='complex_detail'),
    # path('complex/manage/<int:pk>', views.HousingComplexManageView.as_view(), name='complex_manage'),
    # path('house/<int:pk>', views.HouseDetailView.as_view(), name='house_detail'),
    # path('house/manage/<int:pk>', views.HouseManageView.as_view(), name='house_manage'),
    # path('resident/', views.ResidentShortListView.as_view(), name='resident_list'),
    # path('resident/<int:pk>', views.ResidentShortDetailView.as_view(), name='resident_detail'),
    # path('resident/secure/', views.ResidentFullListView.as_view(), name='resident_full_list'),
    # path('resident/secure/<int:pk>', views.ResidentFullDetailView.as_view(), name='resident_full_detail'),
    # path('resident/manage/<int:pk>', views.ResidentManageView.as_view(),
    #      name='resident_full_detail_manage'),
    # path('resident/create/', views.ResidentCreateView.as_view(), name='resident_create'),
    # path('resident/delete/<int:pk>', views.ResidentDeleteView.as_view(), name='resident_delete'),
    # path('status/', views.ExecutionStatusListView.as_view(), name='status_list'),
    # path('status/<int:pk>', views.ExecutionStatusDetailView.as_view(), name='status_detail'),
    # path('status/manage/<int:pk>', views.ExecutionStatusManageView.as_view(), name='status_manage'),
    # path('status/create/', views.ExecutionStatusCreateView.as_view(), name='status_create'),
    # path('status/delete/<int:pk>', views.ExecutionStatusDeleteView.as_view(), name='status_delete'),
    # path('department/<int:pk>', views.DepartmentDetailView.as_view(), name='department_detail'),
    # path('department/manage/<int:pk>', views.DepartmentManageView.as_view(), name='department_manage'),
    # path('position/<int:pk>', views.PositionDetailView.as_view(), name='position_detail'),
    # path('position/manage/<int:pk>', views.PositionManageView.as_view(), name='position_manage'),
    # path('employee/<int:pk>', views.EmployeeShortDetailView.as_view(), name='employee_detail'),
    # path('employee/secure/', views.EmployeeFullListView.as_view(), name='employee_full_list'),
    # path('employee/secure/<int:pk>', views.EmployeeFullDetailView.as_view(), name='employee_full_detail'),
    # path('employee/manage/<int:pk>', views.EmployeeManageView.as_view(),
    #      name='employee_full_detail_manage'),
    # path('service/<int:pk>', views.ServiceDetailView.as_view(), name='service_detail'),
    # path('service/manage/<int:pk>', views.ServiceManageView.as_view(), name='service_manage'),
    # path('request/', views.RequestListView.as_view(), name='request_list'),
    # path('request/manage/<int:pk>', views.RequestManageView.as_view(), name='request_manage'),
    # path('request/delete/<int:pk>', views.RequestDeleteView.as_view(), name='request_delete'),
]
