'''Suvjazi App URL's'''

from django.urls import path, re_path
from suvjazi_app import views

urlpatterns = [
    path('', views.suvjazi_app, name='suvjazi_app'),
    path('person/<slug:person_slug>', views.show_persons, name='show_persons'),
    path('add_person', views.add_person, name='add_person')
]
