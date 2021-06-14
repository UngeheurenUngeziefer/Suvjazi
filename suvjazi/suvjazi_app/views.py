'''Suvjazi_app Views'''

from django.forms.models import inlineformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from suvjazi_app.models import Person, Company, CompanyMembership
from suvjazi_app.forms import PersonForm, CompanyForm, CompanyMembershipForm
from suvjazi.views import index
from django.contrib import messages
from django.forms import modelformset_factory
from django.urls import reverse


def suvjazi_app(request):
    return render(request, 'suvjazi/suvjazi_app.html')


def show_persons(request):
    if request.method == "GET":
        persons_list = Person.objects.order_by('last_name')
        context = {'persons': persons_list}
        return render(request, 'suvjazi/persons.html', context=context)


def show_person(request, slug):
    try:
        person = Person.objects.get(slug=slug)
        person_companies = Company.objects.filter(person=person)
        company_memberships = CompanyMembership.objects.filter(person=person)
        context = {
            'person_companies': person_companies,
            'person': person,
            'company_memberships': company_memberships
            }
    except Person.DoesNotExist:
        context = {
            'person_companies': person_companies,
            'person': person
            }
    return render(request, 'suvjazi/person.html', context)


def add_person(request):
    if request.method == 'GET':
        form = PersonForm()
        form_company_factory = inlineformset_factory(Person, Company.person.through, form=CompanyMembershipForm, extra=1)
        form_company = form_company_factory()
        context = {
            'form': form,
            'form_company': form_company
        }
        return render(request, 'suvjazi/add_person.html', context)
    elif request.method == 'POST':
        form = PersonForm(request.POST)
        form_company_factory = inlineformset_factory(Person, Company.person.through, form=CompanyMembershipForm)
        form_company = form_company_factory(request.POST)
        if form.is_valid() and form_company.is_valid():
            person = form.save()
            form_company.instance = person
            form_company.save()
            return redirect(reverse('show_persons'))
        else:
            context = {
            'form': form,
            'form_company': form_company
            }    
            print(form.errors)
            return render(request, 'suvjazi/add_person.html', context)


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
