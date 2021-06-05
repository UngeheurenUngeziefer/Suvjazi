'''Suvjazi URL's'''

from django.urls import path, re_path
from suvjazi_app import views

urlpatterns = [
    path('', views.suvjazi_app, name='suvjazi_app'),
    path('<slug:person_slug>', views.show_persons, name='show_persons')
]
