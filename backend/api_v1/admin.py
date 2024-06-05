from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.safestring import mark_safe


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ['name']
    list_per_page = 10
    search_fields = [
        'name'
    ]
    save_on_top = True

    class Meta:
        model = City


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    fields = ['name', 'city']
    list_display = ('name', 'city',)
    list_display_links = ('name', 'city',)
    ordering = ['name', 'city']
    list_per_page = 10
    search_fields = [
        'name',
        'city__name'
    ]
    save_on_top = True

    class Meta:
        model = Street


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    fields = ['street', 'number', 'corpus']
    search_fields = [
        'street__name',
        'street__city__name',
        'number'
    ]
    ordering = ['street', 'number']
    list_per_page = 10
    save_on_top = True

    class Meta:
        model = Building


class WorkDayInline(admin.TabularInline):
    model = WorkDay
    extra = 7
    min_num = 7
    max_num = 7
    verbose_name = 'День недели'
    verbose_name_plural = 'Дни недели'
    can_delete = False


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    inlines = []
    save_on_top = True

    def get_inline_instances(self, request, obj=None):
        if obj and obj.name:
            self.inlines = [WorkDayInline]
        else:
            self.inlines = []
        return super().get_inline_instances(request, obj)

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         super().save_model(request, obj, form, change)
    #         for day_of_week in range(1, 8):
    #             WorkDay.objects.create(schedule=obj, day_of_week=day_of_week, is_not_working=True)
    #     else:
    #         super().save_model(request, obj, form, change)

    class Meta:
        model = WorkSchedule


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = [
        'name',
        'address__street__name',
        'address__street__city__name',
        'address__number'
    ]
    readonly_fields = ['display_related_employees']

    def display_related_employees(self, obj):
        employees = Employee.objects.filter(office=obj)
        employee_links = [
            (f'<a href="{reverse("admin:api_v1_employee_change", args=(employee.id,))}">'
             f'{employee.position.name}: {employee}</a>')
            for employee in employees
        ]
        return mark_safe('<br>'.join(employee_links))

    display_related_employees.short_description = "Сотрудники"

    class Meta:
        model = Office


@admin.register(HousingComplex)
class HousingComplexAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = [
        'name',
        'office__name',
        'street__name',
        'street__city__name'
    ]
    readonly_fields = ['display_related_houses']

    def display_related_houses(self, obj):
        houses = House.objects.filter(complex=obj)
        employee_links = [
            (f'<a href="{reverse("admin:api_v1_house_change", args=(house.id,))}">'
             f'{house.address.__str__()}</a>')
            for house in houses
        ]
        return mark_safe('<br>'.join(employee_links))

    display_related_houses.short_description = "Дома"

    class Meta:
        model = HousingComplex


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = [
        'complex__name',
        'address__street__city__name',
        'address__street__name',
        'address__number',
        'address__corpus',
    ]

    class Meta:
        model = House


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ['surname', 'name', 'patronymic', 'phone', 'tg_id']
    search_fields = [
        'name',
        'surname',
        'patronymic',
        'phone',
        'tg_id',
    ]

    class Meta:
        model = Resident


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ['name']
    list_per_page = 10
    search_fields = ['name']
    save_on_top = True

    class Meta:
        model = Department


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    fields = ['name', 'department']
    list_display = ('name', 'department',)
    list_display_links = ('name', 'department',)
    ordering = ['name', 'department']
    list_per_page = 10
    search_fields = ['name', 'department__name']
    save_on_top = True

    class Meta:
        model = Position


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['surname', 'name', 'patronymic', 'phone', 'email', 'office', 'position', 'tg_id']
    list_per_page = 10
    search_fields = [
        'name',
        'surname',
        'patronymic',
        'phone',
        'email',
        'office__name',
        'office__address__street__city__name',
        'office__address__street__name',
        'office__address__number',
        'office__address__corpus',
        'position__name',
        'position__department__name',
        'tg_id',
    ]
    save_on_top = True

    class Meta:
        model = Employee


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'display_photo']
    list_per_page = 10
    search_fields = [
        'text',
        'status__name',
        'resident__name',
        'resident__surname',
        'resident__patronymic',
        'resident__phone',
        'resident__tg_id',
        'address__complex__name',
        'address__address__street__city__name',
        'address__address__street__name',
        'address__address__number',
        'address__address__corpus',
        'apartment',
        'employee__name',
        'employee__surname',
        'employee__patronymic',
        'employee__phone',
        'employee__email',
        'employee__office__name',
        'employee__office__address__street__city__name',
        'employee__office__address__street__name',
        'employee__office__address__number',
        'employee__office__address__corpus',
        'employee__position__name',
        'employee__position__department__name',
        'employee__tg_id',
        'service__name'
    ]
    save_on_top = True

    def display_photo(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60">')

    display_photo.short_description = 'Фото обращения'

    class Meta:
        model = Request


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = [
        'name',
        'description',
        'position__name',
        'position__department__name'
    ]
    save_on_top = True

    class Meta:
        model = Service


@admin.register(RequestTask)
class RequestTaskAdmin(admin.ModelAdmin):
    list_per_page = 10
    # search_fields = [
    #     'name',
    #     'description',
    #     'position__name',
    #     'position__department__name'
    # ]
    save_on_top = True

    class Meta:
        model = RequestTask


admin.site.register(ExecutionStatus)
admin.site.register(BotsSettings)
