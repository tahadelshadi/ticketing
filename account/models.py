from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class User(AbstractUser):
    department = models.ForeignKey('Department',verbose_name=_("دپارتمان"), on_delete=models.SET_NULL,null=True,blank=True)
    is_supporter = models.BooleanField(_("پشتیبانی"),default=False)
    
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"

class Department(models.Model):
    creator = models.ForeignKey(User,verbose_name=_("سازنده"),related_name='creator+', on_delete=models.CASCADE)
    name = models.CharField(_("نام"),max_length=55)

    class Meta:
        verbose_name = "دپارتمان"
        verbose_name_plural = "دپارتمان ها"

    def __str__(self):
        return self.name