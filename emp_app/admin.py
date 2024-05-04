from django.contrib import admin
from .models import Department, Role, Employee

# Register your models here.
admin.site.register(Department)
admin.site.register(Role)
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display =  ['id','first_name','last_name','phone','dept','role','salary','bonus','hire_date']