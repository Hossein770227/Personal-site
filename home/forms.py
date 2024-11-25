from django import forms

from .models import Customer_call


class UserMessageForm(forms.ModelForm):
    class Meta:
        model = Customer_call
        fields = ['full_name','phone_number','message',]
        