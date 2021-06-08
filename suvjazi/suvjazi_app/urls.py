'''Suvjazi App URL's'''

from django.urls import path
from suvjazi_app import views

urlpatterns = [
    path('', views.suvjazi_app, name='suvjazi_app'),
    path('persons/', views.show_persons, name='show_persons'),
    path('persons/add_person', views.add_person, name='add_person'),
    path('persons/<slug:person_slug>', views.show_person, name='show_person'),
    path('persons/<slug:person_slug>/edit', views.edit_person, 
                                            name='edit_person'),

    path('companies/', views.show_companies, name='show_companies'),
    path('companies/add_company', views.add_company, name='add_company'),
    path('companies/<slug:company_slug>', views.show_company, 
                                          name='show_company')
]
