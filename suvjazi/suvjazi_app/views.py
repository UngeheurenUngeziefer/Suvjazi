'''Suvjazi_app Views'''

from django.forms.models import inlineformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from suvjazi_app.models import Person, Company, CompanyMembership
from suvjazi_app.forms import PersonForm, CompanyForm, CompanyMembershipForm
from suvjazi.views import index
from django.contrib import messages
from django.forms import modelformset_factory
from django.urls import reverse

from django.shortcuts import render, redirect

from django.views.generic import ListView, TemplateView, View
from django.views.generic.edit import UpdateView, DeleteView
from typing import Union, List
from django.db.models import QuerySet

from django.urls import reverse_lazy

from django.http import JsonResponse



class ViewSuvjaziApp(View):
    # view for SuvjaziApp page
    def get(self, request):
        return render(request, 'suvjazi/suvjazi_app.html')


class ListEntities(ListView):
    # class for showing list of entities with sorting
    def __init__(self,
                 model: Union[Person, Company], 
                 template_name: str, 
                 sort_field: str, 
                 jinja_obj: str):

        self.model = model
        self.template_name = template_name
        self.sort_field = sort_field
        self.jinja_obj = jinja_obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entities_list = self.model.objects.order_by(self.sort_field)
        context[self.jinja_obj] = entities_list
        return context


class ListPersons(ListEntities):
    def __init__(self):
        self.model = Person
        self.template_name = 'suvjazi/persons.html'
        self.sort_field = 'last_name'
        self.jinja_obj = 'persons'


class ListCompanies(ListEntities):
    # parent class to list entities
    def __init__(self):
        self.model = Company
        self.template_name = 'suvjazi/companies.html'
        self.sort_field = 'company_name'
        self.jinja_obj = 'companies'


class ViewPerson(TemplateView):
    # class for showing one Person from the list of
    def __init__(self):
        self.template_name = 'suvjazi/person.html'

        
    def get_context_data(self, slug, **kwargs):
        context = super().get_context_data(**kwargs)
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
            context = {}
        return context

        
class ViewInstitute(TemplateView):
    # class for showing one Institute from the list
    def __init__(self,
                 model: Union[Company],
                 template_name: str,
                 entity_persons: Union[QuerySet, List[Person]]):
        
        self.model = model
        self.template_name = template_name
        self.entity_persons = entity_persons
        

    def get_context_data(self, slug, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            entity_persons, entity = self.entity_persons_queryset(slug)
            context = {
                'entity_persons': entity_persons,
                'entity': entity
            }
        except self.model.DoesNotExist:
            context = {}
        return context


class ViewCompany(ViewInstitute):
    def __init__(self):
        self.model = Company
        self.template_name = 'suvjazi/company.html'

    def entity_persons_queryset(self, slug):
        entity = self.model.objects.get(slug=slug)
        entity_persons = Person.objects.filter(company=entity)
        return entity_persons, entity


class CreatePerson(CreateView):
    # create person view
    def get(self, request, *args, **kwargs):
        form = PersonForm()
        form_company_factory = inlineformset_factory(Person, Company.person.through, form=CompanyMembershipForm, extra=1)
        form_company = form_company_factory()
        

        context = {
            'form': form,
            'form_company': form_company
        }
        return render(request, 'suvjazi/add_person.html', context)

    def post(self, request, *args, **kwargs):
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


class CreateInstitute(CreateView):
    # parent view to create institute

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})

    def post_generalizer(self, request, *args, **kwargs):
        if self.form.is_valid():
            self.form.save(commit=True)
            return redirect(self.redirect_path)
        else:
            print(self.form.errors)
        return render(request, self.template_name, {'form': self.form})

  
class CreateCompany(CreateInstitute):
    # company creation view

    def __init__(self):
        self.model = Company
        self.template_name = 'suvjazi/add_company.html'
        self.form = CompanyForm()
        self.redirect_path = 'show_companies'

    def post(self, request, *args, **kwargs):
        self.form = CompanyForm(request.POST)
        return self.post_generalizer(self, request, *args, **kwargs)
        

class UpdatePerson(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'suvjazi/edit_person.html'

    def post(self, request, slug, *args, **kwargs):
        person = get_object_or_404(Person, slug=slug)
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Changes saved.')
            return redirect('show_persons')
        else:
            form = PersonForm(instance=person)
            print(form.errors)
            return render(request, self.template_name, {'form': form})


class UpdateInstitute(UpdateView):

    def __init__(self, model, form_class, template_name):
        self.model = model
        self.form_class = form_class
        self.template_name = template_name

    def post(self, request, slug, *args, **kwargs):
        form = self.entity_edit_query_set(request, slug)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Changes saved.')
            return redirect(self.redirect_page)
        else:
            print(form.errors)
            return render(request, self.template_name, {'form': form})


class UpdateCompany(UpdateInstitute):

    def __init__(self):
        self.model = Company
        self.form_class = CompanyForm
        self.template_name = 'suvjazi/edit_company.html'
        self.redirect_page = 'show_companies'


    def entity_edit_query_set(self, request, slug):
        company = get_object_or_404(Company, slug=slug)
        form = CompanyForm(request.POST, instance=company)
        return form
    

class DeleteEntity(DeleteView):
    
    def __init__(self, model, success_url, template_name):
        self.model = model
        self.success_url = success_url
        self.template_name = template_name

    def post(self, request, slug, *args, **kwargs):
        entity, entity_str, entity_name  = self.delete_entity_query_set(slug)
        entity.delete()
        messages.add_message(request, messages.INFO,
                                    f'{entity_str} "{entity_name}" successfully deleted.')
        return redirect(self.redirect_page)


class DeletePerson(DeleteEntity):
    
    def __init__(self):
        self.model = Person
        self.success_url = reverse_lazy('delete_person')
        self.template_name = 'suvjazi/delete_person.html'
        self.redirect_page = 'show_persons'

    def delete_entity_query_set(self, slug):
        person = get_object_or_404(Person, slug=slug)
        entity_str = 'Person'
        entity_name = person.full_name
        return person, entity_str, entity_name


class DeleteCompany(DeleteEntity):

    def __init__(self):
        self.model = Company
        self.success_url = reverse_lazy('delete_company')
        self.template_name = 'suvjazi/delete_company.html'
        self.redirect_page = 'show_companies'

    def delete_entity_query_set(self, slug):
        company = get_object_or_404(Company, slug=slug)
        entity_str = 'Company'
        entity_name = company.company_name
        return company, entity_str, entity_name
