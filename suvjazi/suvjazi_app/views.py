'''Suvjazi_app Views'''

from django.shortcuts import render
from django.http import HttpResponse
from suvjazi_app.models import Person, Company, CompanyMembership


def suvjazi(request):
    # construct a dictionary to pass to the template engine as its context
    persons_list = Person.objects.order_by('last_name')
    companies_list = Company.objects.order_by('company_name')
    context_dict = {'persons': persons_list, 'companies': companies_list}
    
    return render(request, 'suvjazi/suvjazi_app.html', context=context_dict)
