'''Suvjazi_app Views'''

from django.forms.models import inlineformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from suvjazi_app.models import Person, Company, CompanyMembership
from suvjazi_app.forms import PersonForm, CompanyForm
from suvjazi.views import index
from django.contrib import messages
from django.forms import modelformset_factory


def suvjazi_app(request):
    return render(request, 'suvjazi/suvjazi_app.html')


def show_persons(request):
    persons_list = Person.objects.order_by('last_name')
    context_dist = {'persons': persons_list}
    return render(request, 'suvjazi/persons.html', context=context_dist)


def show_person(request, slug):
    context_dict = {}
    try:
        person = Person.objects.get(slug=slug)
        person_companies = Company.objects.filter(person=person)
        context_dict['person_companies'] = person_companies
        context_dict['person'] = person
    except Person.DoesNotExist:
        context_dict['person'] = None
        context_dict['person_companies'] = None
    
    return render(request, 'suvjazi/person.html', context_dict)


def add_person(request):
    form = PersonForm()
    form_company_factory = inlineformset_factory(Person, CompanyMembership, form=CompanyForm, extra=3)
    form_company = form_company_factory()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid() and form_company.is_valid():
            person = form.save()
            form_company.instance = person
            form_company.save()
            return show_persons(request)
        else:
            print(form.errors)
    return render(request, 'suvjazi/add_person.html', {'form': form, 'form_company': form_company})


def edit_person(request, slug):
    person = get_object_or_404(Person, slug=slug)
    form = PersonForm()

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
                                    f'Changes saved.')
            return redirect('show_persons')
    else:
        form = PersonForm(instance=person)
        print(form.errors)
        return render(request, 'suvjazi/edit_person.html', {'form': form})


def delete_person(request, slug):
    person = get_object_or_404(Person, slug=slug)
    full_name = person.full_name
    if request.method == 'POST':
        person.delete()
        messages.add_message(request, messages.INFO,
                                    f'Person {full_name} successfully deleted.')
        return redirect('show_persons')

    return render(request, 'suvjazi/delete_person.html', {'person': person})


def show_companies(request):
    companies_list = Company.objects.order_by('company_name')
    context_dict = {'companies': companies_list}
    
    return render(request, 'suvjazi/companies.html', context=context_dict)


def show_company(request, slug):
    context_dict = {}
    try:
        company = Company.objects.get(slug=slug)
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


def edit_company(request, slug):
    company = get_object_or_404(Company, slug=slug)
    form = CompanyForm()

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
                                    f'Changes saved.')
            return redirect('show_companies')
    else:
        form = CompanyForm(instance=company)
        print(form.errors)
        return render(request, 'suvjazi/edit_company.html', {'form': form})


def delete_company(request, slug):
    company = get_object_or_404(Company, slug=slug)
    company_name = company.company_name
    if request.method == 'POST':
        company.delete()
        messages.add_message(request, messages.INFO,
                                f'Company {company_name} successfully deleted.')
        return redirect('show_companies')

    return render(request, 'suvjazi/delete_company.html', {'company': company})
