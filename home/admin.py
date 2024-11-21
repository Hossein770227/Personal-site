from django.contrib import admin
from django.contrib.auth.models import Group, User
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
   list_display = ['name_customer', 'date_time_created']



   admin.site.unregister(User)
admin.site.unregister(Group)
