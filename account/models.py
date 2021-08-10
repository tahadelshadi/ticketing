from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
# Create your models here.

class User(AbstractUser):
    is_sup = models.BooleanField(_('دپارتمان پشتیبانی'), default=False)
    is_accountants = models.BooleanField(_('دپارتمان حسابداری'), default=False)
