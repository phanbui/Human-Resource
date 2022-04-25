from django.contrib import admin

# Register your models here.

from .models import *
import nested_admin
from django_admin_listfilter_dropdown.filters import *
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.forms import TextInput, Textarea

# Register your models here.

admin.site.site_header = 'Polygot Human Resource'
admin.site.index_title = 'Polygot Human Resource Admin'

class SquadInLineStaff(admin.TabularInline):
    model = StaffTimeAllocation
    extra = 0

class StaffAdmin(admin.ModelAdmin):
    # All staff view
    list_display = ('name', 'staff_id', 'position', 'salary', 'date_hired')
    ordering = ['name']
    list_filter = (('position', DropdownFilter),)
    search_fields = ('name', 'staff_id', 'position', 'salary', 'date_hired')

    # Change staff view
    fields = ('name', 'staff_id', 'position', 'salary', 'date_hired', 'note')
    inlines = [
        SquadInLineStaff,
    ]

class StaffInLineSquad(admin.TabularInline):
    model = StaffTimeAllocation
    extra = 0
    # Query optimization
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('staff', 'squad')

class SquadAdmin(admin.ModelAdmin):
    # All squad view
    list_display = ('name', 'description', 'project', 'note', 'staffs')
    ordering = ['name']
    list_filter = (('project', RelatedDropdownFilter),)
    search_fields = ('name', 'description', 'note')
    
    inlines = [
        StaffInLineSquad,
    ]

class StaffTimeAllocationInline(nested_admin.NestedTabularInline):
    model = StaffTimeAllocation
    extra = 0
    # Query optimization
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('staff', 'squad')

class SquadInLineProject(nested_admin.NestedTabularInline):
    model = Squad
    extra = 0
    # sortable_field_name = "position"
    inlines = [StaffTimeAllocationInline]

class ProjectAdmin(nested_admin.NestedModelAdmin):
    ordering = ['name']
    search_fields = ('name', 'project_id', 'status', 'category', 'start_date', 'end_date', 'description', 'note')

    inlines = [SquadInLineProject,]

admin.site.register(Staff, StaffAdmin)
admin.site.register(Squad, SquadAdmin)
admin.site.register(Project, ProjectAdmin)

# Citation: https://github.com/phanbui/tcb-hr