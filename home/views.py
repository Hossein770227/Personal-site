from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Portfolio

class HomePage(ListView):
    model = Portfolio
    template_name = 'home/home.html'
    context_object_name = 'portfolio'
    