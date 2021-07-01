from django import forms
from django.forms.widgets import Widget
from suvjazi_app.models import Person, Company, CompanyMembership
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.contrib.admin import site as admin_site


class PersonForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128,
                                 help_text='First name:')
    last_name  = forms.CharField(max_length=128,
                                 help_text='Last name:')
    
    class Meta:
    # Provide an association between the ModelForm and a model
        model   = Person
        fields  = ('first_name', 'last_name')
        exclude = ('slug', )
        
    
class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(
                    max_length=100,
                    widget=forms.TextInput(attrs={
                        'placeholder': 'Company Name',
                    }),
                    required=False)
    company_url = forms.URLField(
                        max_length=200,
                        required=False)
    person = forms.ModelMultipleChoiceField(
                        queryset=Person.objects.all(),
                        widget=forms.CheckboxSelectMultiple,
                        help_text='Add existing persons from this company',
                        required=False)
                                 
    class Meta:
        model = Company
        fields = ('company_name', 'company_url', 'person')
        exclude = ('slug', )

    def clean(self):
        # checks if https added on url field
        cleaned_data = self.cleaned_data
        company_url = cleaned_data.get('company_url')
        if company_url and not company_url.startswith('http://') \
                       and not company_url.startswith('https://'):
            company_url = 'http://' + company_url
            cleaned_data['company_url'] = company_url
        return cleaned_data



class CompanyMembershipForm(forms.ModelForm):
    person = forms.ModelMultipleChoiceField(
                        queryset=Person.objects.all(),
                        widget=forms.CheckboxSelectMultiple,
                        help_text='Add existing persons from this company',
                        required=False)
    company = forms.ModelChoiceField(
                    queryset=Company.objects.all().order_by('company_name'),
                    required=False,
                    )
    
    date_joined = forms.DateField()
    date_leaved = forms.DateField()
    job_functions_description = forms.Textarea()
    
    class Meta:
        model   = CompanyMembership
        fields  = '__all__'
       