from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_page_view, name = 'home'),
    # path('message/', views.message_from_user, name='message_user'),
]

