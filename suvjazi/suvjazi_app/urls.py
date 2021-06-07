'''Suvjazi App URL's'''

from django.urls import path, re_path
from suvjazi_app import views

urlpatterns = [
    path('', views.suvjazi_app, name='suvjazi_app'),
    path('person/<slug:person_slug>', views.show_person, name='show_person'),
    path('add_person', views.add_person, name='add_person'),
    path('company/<slug:company_slug>', views.show_company, name='show_company')
]
