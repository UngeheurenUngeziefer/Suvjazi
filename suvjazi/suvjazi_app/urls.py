'''Suvjazi URL's'''

from django.urls import path
from suvjazi_app import views

urlpatterns = [
    path('', views.suvjazi, name='suvjazi'),
    path('about', views.about, name='about')
]