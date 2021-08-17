from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','first_name','last_name','department','is_staff')

class DepartmentAdmin(admin.ModelAdmin):
    list_display=('name','creator')


admin.site.register(Department,DepartmentAdmin)    
admin.site.register(User,UserAdmin)