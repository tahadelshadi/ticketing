from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','first_name','last_name','is_accountants','is_sup','is_staff',)

    
admin.site.register(User,UserAdmin)