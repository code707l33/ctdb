from django.db import models
from django.utils.translation import gettext_lazy as _


class Pilotadmin(models.Model):

    customer_name = models.CharField(verbose_name=_('Customer Name'), max_length=50)
    bg_name = models.CharField(verbose_name=_('BG name'), max_length=50)
    direct_number = models.CharField(verbose_name=_('Direct Number'), max_length=20)
    adminpassword = models.CharField(verbose_name=('Admin Password'), max_length=20)