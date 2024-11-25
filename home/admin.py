from django.contrib import admin
from django.contrib.auth.models import Group, User
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Customer_call, Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
   list_display = ['name_customer', 'date_time_created']



@admin.register(Customer_call)
class MessageUser(admin.ModelAdmin):
   list_display =['full_name','phone_number','date_time_send_message',]



   admin.site.unregister(User)
admin.site.unregister(Group)
