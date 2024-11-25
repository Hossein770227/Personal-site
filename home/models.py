from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _



class Portfolio(models.Model):
    name_customer = models.CharField(_("customer name"), max_length=255, blank=True)
    image = models.ImageField(verbose_name=_('image'), upload_to='cover/')
    date_time_created = models.DateTimeField(_("date created"), default=timezone.now)

    class Meta:
        verbose_name = _('portfolio')
        verbose_name_plural = _('portfolio')


class Customer_call(models.Model):
    full_name = models.CharField(_("full name"), max_length=100)
    phone_number = models.CharField(_("phone number"), max_length=11)
    message = models.TextField(_("message"))
    date_time_send_message = models.DateTimeField(_("date send message"),  auto_now_add=True)
    
    class Meta:
        verbose_name = _('message from user')
        verbose_name_plural = _('message from user')

    def __str__(self):
        return self.full_name
