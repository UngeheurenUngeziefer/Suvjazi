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
    company_name = forms.CharField(max_length=128, 
                                   help_text="Please enter the company name.")
    company_url = forms.URLField(max_length=200, required=False)
                                 
    class Meta:
        model = Company
        fields = ('company_name', 'company_url')
        exclude = ('person', 'slug')
    

    def clean(self):
        cleaned_data = self.cleaned_data
        company_url = cleaned_data.get('company_url')
        if company_url and not company_url.startswith('http://'):
            company_url = 'http://' + company_url
            cleaned_data['company_url'] = company_url
        return cleaned_data