'''Suvjazi App URL's'''

from django.urls import path
from suvjazi_app import views

from django.urls import include, path

from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.SuvjaziApp.as_view(), name='suvjazi_app'),
    path('persons/', views.ListPersons.as_view(), name='show_persons'),
    path('persons/add_person', views.CreatePerson.as_view(), name='add_person'),
    path('persons/<slug:slug>', views.ViewPerson.as_view(), name='show_person'),
    path('persons/<slug:slug>/edit', views.edit_person, 
                                            name='edit_person'),
    path('persons/<slug:slug>/delete', views.delete_person,
                                              name='delete_person'),

    path('companies/', views.ListCompanies.as_view(), name='show_companies'),
    path('companies/add_company', views.CreateInstitute.as_view(), name='add_company'),
    path('companies/<slug:slug>', views.ViewCompany.as_view(), name='show_company'),
    path('companies/<slug:slug>/edit', views.edit_company, name='edit_company'),
    path('companies/<slug:slug>/delete', views.delete_company, 
                                          name='delete_company'),
    
]
