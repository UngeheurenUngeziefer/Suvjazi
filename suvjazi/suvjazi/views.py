'''General Views'''
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Construct a dictionary to pass to the template engine as its context
    context_dict = {'boldmessage': 'Value of boldmessage!'}
    
    return render(request, 'suvjazi/index.html', context=context_dict)
