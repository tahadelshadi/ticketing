from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user','title','sup_type','content','pb_date','status',)
    # list_filter = ('publish','status', )
    # search_fields = ('title', 'description')
    # ordering = ['-status', '-publish']

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('ticket','user','content','pb_date',)
    ordering = ['-pb_date']

UserAdmin.fieldsets += (
    ("نوع دپارتمان", { "fields": ('is_sup', 'is_accountants' )}),
)



admin.site.register(Ticket,TicketAdmin)
admin.site.register(Response,ResponseAdmin)