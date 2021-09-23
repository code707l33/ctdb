from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Pilotadmin(models.Model):

    customer_name = models.CharField(verbose_name=_('Customer Name'), max_length=50)
    bg_name = models.CharField(verbose_name=_('BG name'), max_length=50)
    direct_number = models.CharField(verbose_name=_('Direct Number'), max_length=20)
    adminpassword = models.CharField(verbose_name=('Admin Password'), max_length=20)

    class Meta:
        verbose_name = _('Pilot Admin')
        verbose_name_plural = _('Pilot Admin')

    def __str__(self):
        return self.customer_name

    def get_create_url(self):
        return reverse('pilotadmin:pilotadmin_create')

    def get_update_url(self):
        return reverse('pilotadmin:pilotadmin_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('pilotadmin:pilotadmin_delete', kwargs={'pk': self.pk})
