'''Suvjazi App URL's'''

from django.urls import path
from suvjazi_app import views

urlpatterns = [
    path('', views.suvjazi_app, name='suvjazi_app'),
    path('persons/', views.show_persons, name='show_persons'),
    path('persons/add_person', views.add_person, name='add_person'),
    path('persons/<slug:slug>', views.show_person, name='show_person'),
    path('persons/<slug:slug>/edit', views.edit_person, 
                                            name='edit_person'),
    path('persons/<slug:slug>/delete', views.delete_person,
                                              name='delete_person'),

    path('companies/', views.show_companies, name='show_companies'),
    path('companies/add_company', views.add_company, name='add_company'),
    path('companies/<slug:slug>', views.show_company, name='show_company'),
    path('companies/<slug:slug>/edit', views.edit_company, name='edit_company'),
    path('companies/<slug:slug>/delete', views.delete_company, 
                                          name='delete_company')
    
]
