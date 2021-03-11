from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import validate_comma_separated_prefix_list_string
from .validators import validate_semicolon_seperated_email_string


class Isp(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=63)
    cname = models.CharField(verbose_name=_('Chinese Name'), max_length=63)
    customer_no = models.CharField(verbose_name=_('Customer No.'), max_length=63)
    upstream_as = models.CharField(verbose_name=_('Upstream AS'), max_length=63)
    primary_contact = models.CharField(verbose_name=_('Primary contact'), max_length=63)
    to = models.TextField(verbose_name=_('To'), blank=True, validators=[validate_semicolon_seperated_email_string, ])
    cc = models.TextField(verbose_name=_('CC'), blank=True, validators=[validate_semicolon_seperated_email_string, ])
    bcc = models.TextField(verbose_name=_('BCC'), blank=True, validators=[validate_semicolon_seperated_email_string, ])
    telephone = models.CharField(verbose_name=_('Telephone'), max_length=63, blank=True)
    cellphone = models.CharField(verbose_name=_('Cellphone'), max_length=63, blank=True)
    remark = models.TextField(verbose_name=_('Remark'), blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class IspGroup(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=63)
    isps = models.ManyToManyField(verbose_name=_('ISPs'), to='telecom.Isp')
    remark = models.TextField(verbose_name=_('Remark'), blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def isps_as_str(self):
        return ',\n'.join(instance.name for instance in self.isps.all())


class PrefixListUpdateTask(models.Model):
    update_type = models.CharField(
        verbose_name=_('Update type'),
        max_length=63,
        choices=(
            ('add prefix-list', _('Add prefix-list')),
            ('add as', _('Add AS')),
            ('add route', _('Add Route')),
        )
    )
    isps = models.ManyToManyField(verbose_name=_('ISPs'), to='telecom.Isp', blank=True)
    isp_groups = models.ManyToManyField(verbose_name=_('ISP groups'), to='telecom.IspGroup', blank=True)
    origin_as = models.CharField(verbose_name=_('Origin AS'), max_length=63)
    as_path = models.CharField(verbose_name=_('AS path'), max_length=63)
    prefix_list = models.TextField(verbose_name=_('Prefix-list'), validators=[validate_comma_separated_prefix_list_string, ])
    remark = models.TextField(verbose_name=_('Remark'), blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def isps_as_str(self):
        return ',\n'.join(instance.name for instance in self.isps.all())

    def isp_group_as_str(self):
        return ',\n'.join(instance.name for instance in self.isp_groups.all())
