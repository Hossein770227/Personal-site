from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Portfolio
from .forms import UserMessageForm

# class HomePage(ListView):
#     model = Portfolio
#     template_name = 'home/home.html'
#     context_object_name = 'portfolio'
    
# def message_from_user(request):
#     if request.method =='POST':
#         user_message = UserMessageForm(request.POST)
#         if user_message.is_valid():
#             user_message.save()
#             user_message = UserMessageForm()
#         else:
#             user_message = UserMessageForm()
#         return render(request, 'home/home.html',{'form':user_message})

def home_page_view(request):
    portfolio = Portfolio.objects.all()
    if request.method =='POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserMessageForm()
    else:
        form = UserMessageForm()
    return render(request, 'home/home.html', {'form':form, 'portfolio':portfolio})
    
