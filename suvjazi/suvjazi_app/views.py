'''Suvjazi_app Views'''

from django.shortcuts import render
from django.http import HttpResponse

def suvjazi(request):
    return HttpResponse('First text!')

def about(request):
    return HttpResponse('About page!')

