from django import forms
from suvjazi_app.models import Person, Company


class PersonForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128,
                                 help_text='Please enter first name.')
    last_name = forms.CharField(max_length=128,
                                help_text='Please enter last name.')

    class Meta:
     # Provide an association between the ModelForm and a model
        model = Person
        fields = ('first_name', 'last_name')
        exclude = ('slug', )


class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(
                        max_length=128, 
                        help_text="Please enter the company name.")
    company_url = forms.URLField(
                        max_length=200,
                        required=False, 
                        help_text='Company URL')
    person = forms.ModelMultipleChoiceField(
                        queryset=Person.objects.all(),
                        widget=forms.CheckboxSelectMultiple,
                        help_text='Add existing persons from this company')
                                 
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