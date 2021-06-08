'''Suvjazi_app Views'''

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from suvjazi_app.models import Person, Company, CompanyMembership
from suvjazi_app.forms import PersonForm, CompanyForm
from suvjazi.views import index


def suvjazi_app(request):
    # construct a dictionary to pass to the template engine as its context
    persons_list = Person.objects.order_by('last_name')
    companies_list = Company.objects.order_by('company_name')
    context_dict = {'persons': persons_list, 'companies': companies_list}
    
    return render(request, 'suvjazi/suvjazi_app.html', context=context_dict)


def show_persons(request):
    persons_list = Person.objects.order_by('last_name')
    context_dist = {'persons': persons_list}
    return render(request, 'suvjazi/persons.html', context=context_dist)


def show_person(request, person_slug):
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
            return show_persons(request)
        else:
            print(form.errors)
    return render(request, 'suvjazi/add_person.html', {'form': form})


def edit_person(request, person_slug):
    person = get_object_or_404(Person, slug=person_slug)
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return show_persons(request)
        else:
            form = PersonForm(instance=person)
            print(form.errors)
        
    return render(request, 'suvjazi/edit_person.html', {'form': form})


def show_companies(request):
    companies_list = Company.objects.order_by('company_name')
    context_dict = {'companies': companies_list}
    
    return render(request, 'suvjazi/companies.html', context=context_dict)


def show_company(request, company_slug):
    context_dict = {}
    try:
        company = Company.objects.get(slug=company_slug)
        company_persons = Person.objects.filter(company=company)
        context_dict['company_persons'] = company_persons
        context_dict['company'] = company
    except Company.DoesNotExist:
        context_dict['company'] = None
        context_dict['company_persons'] = None
    
    return render(request, 'suvjazi/company.html', context_dict)


def add_company(request):
    form = CompanyForm()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return show_companies(request)
        else:
            print(form.errors)
    return render(request, 'suvjazi/add_company.html', {'form': form})