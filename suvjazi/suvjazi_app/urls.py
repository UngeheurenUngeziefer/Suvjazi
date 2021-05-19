from django.urls import path
from suvjazi_app import views

urlpatterns = [
    path('', views.index, name='index')
]
