'''Suvjazi App URL's'''

from django.urls import path
from suvjazi_app import views

from django.urls import include, path

from django.urls import include, path
from . import views
from suvjazi_app.views import BookListView

urlpatterns = [
    path('', views.ViewSuvjaziApp.as_view(), name='suvjazi_app'),
    path('persons/', views.ListPersons.as_view(), name='show_persons'),
    path('persons/add_person', views.CreatePerson.as_view(), name='add_person'),
    path('persons/<slug:slug>', views.ViewPerson.as_view(), name='show_person'),
    path('persons/<slug:slug>/edit', views.UpdatePerson.as_view(), 
                                            name='edit_person'),
    path('persons/<slug:slug>/delete', views.DeletePerson.as_view(),
                                              name='delete_person'),

    path('companies/', views.ListCompanies.as_view(), name='show_companies'),
    path('companies/add_company', views.CreateCompany.as_view(), name='add_company'),
    path('companies/<slug:slug>', views.ViewCompany.as_view(), name='show_company'),
    path('companies/<slug:slug>/edit', views.UpdateCompany.as_view(), name='edit_company'),
    path('companies/<slug:slug>/delete', views.DeleteCompany.as_view(), 
                                          name='delete_company'),

    path('book', BookListView.as_view(), name='book-list-single'),
    
]
