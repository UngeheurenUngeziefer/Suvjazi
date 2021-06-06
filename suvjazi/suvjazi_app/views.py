'''Suvjazi_app Views'''

from django.shortcuts import render
from django.http import HttpResponse
from suvjazi_app.models import Person, Company, CompanyMembership
from suvjazi_app.forms import PersonForm
from suvjazi.views import index


def suvjazi_app(request):
    # construct a dictionary to pass to the template engine as its context
    persons_list = Person.objects.order_by('last_name')
    companies_list = Company.objects.order_by('company_name')
    context_dict = {'persons': persons_list, 'companies': companies_list}
    
    return render(request, 'suvjazi/suvjazi_app.html', context=context_dict)

def show_persons(request, person_slug):
    context_dict = {}
    try:
        person = Person.objects.get(slug=person_slug)
        person_companies = Company.objects.filter(person=person)
        context_dict['person_companies'] = person_companies
        context_dict['person'] = person
    except Person.DoesNotExist:
        context_dict['person'] = None
        context_dict['person_companies'] = None
    
    return render(request, 'suvjazi/person.html', context_dict)


def add_person(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return suvjazi_app(request)
        else:
            print(form.errors)
    return render(request, 'suvjazi/add_person.html', {'form': form})


