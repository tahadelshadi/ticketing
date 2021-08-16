from django.db import models
from account.models import User
from datetime import datetime
from django.utils.translation import gettext as _
from extensions.utils import jalali_converter
# Create your models here.


class Ticket(models.Model):
    
    user = models.ForeignKey(User, verbose_name=_("کاربر"),default=None, on_delete=models.CASCADE)
    title = models.CharField(_("موضوع"), max_length=50)
    sup_type = models.ForeignKey('Department', verbose_name= _("دپارتمان"), on_delete=models.SET_NULL, blank=True,null=True)
    content = models.TextField(_("پیام"),blank=True,null=True)
    image = models.ImageField(_("عکس"), upload_to='media/ticket',blank=True,null=True)
    pb_date = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=False, default=datetime.now)
    status = models.BooleanField(_("وضعیت تیکت"),default=True)
    
    class Meta:
        verbose_name = "تیکت"
        verbose_name_plural = "تیکت ها"
        ordering = ['-pb_date']


    def __str__(self):
        return self.title
    def jpublish(self):
        return jalali_converter(self.pb_date)
    jpublish.short_description = "زمان انتشار"

class Response(models.Model):
    user = models.ForeignKey(User, verbose_name=_("کاربر"),default=None, on_delete=models.CASCADE)
    ticket = models.ForeignKey("Ticket", verbose_name=_("تیکت"),default=None, on_delete=models.CASCADE)
    content = models.TextField(_("پیام"),blank=True,null=True)
    image = models.ImageField(_("عکس"), upload_to='media/ticket',blank=True,null=True)
    pb_date = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=False, default=datetime.now)
    
    class Meta:
        verbose_name = "جواب"
        verbose_name_plural = "جواب ها"
        ordering = ['-pb_date']

    def jpublish(self):
        return jalali_converter(self.pb_date)
    jpublish.short_description = "زمان انتشار"
    

    def __str__(self):
        return self.content

class Department(models.Model):
    name = models.CharField(_("نام"),max_length=55)
    creator = models.ForeignKey(User,verbose_name=_("سازنده"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "دپارتمان"
        verbose_name_plural = "دپارتمان ها"

    def __str__(self):
        return self.name