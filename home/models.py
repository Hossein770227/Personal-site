from django.db import models
from django.utils.translation import gettext as _


class Portfolio(models.Model):
    name_customer = models.CharField(_("customer name"), max_length=255, blank=True)
    image = models.ImageField(verbose_name=_('image'), upload_to='cover/')
    date_time_created = models.DateTimeField(_("date created"), auto_now_add=True)

    class Meta:
        verbose_name = _('portfolio')
        verbose_name_plural = _('portfolio')
