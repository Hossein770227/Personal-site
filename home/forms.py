from django import forms

from .models import Customer_call


class UserMessageForm(forms.ModelForm):
    class Meta:
        model = Customer_call
        fields = ['full_name','phone_number','message',]
        # widgets = {
        #     'address':forms.Textarea(attrs={'rows':4, 'placeholder':_('please enter your address here')}),
        #     'order_notes':forms.Textarea(attrs={'rows':3,'placeholder':_('please enter your notes here otherwise Leave blank')}),
        #     }