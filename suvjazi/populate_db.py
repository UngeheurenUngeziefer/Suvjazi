# update script - change logic from company->persons to person->companies

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'suvjazi.settings')

import django
django.setup()

from suvjazi_app.models import Company, Person

def populate_db():
    # function to automatic population of django app db
    companyOne_people = [
        {'first_name': 'Oleg',
         'last_name': 'Devyatov'},
        {'first_name': 'Anna',
         'last_name': 'Smith'},
        {'first_name': 'Ellie',
         'last_name': 'Stockholm'}]

    companyTwo_people = [
        {'first_name': 'Kristina',
         'last_name': 'Alova'},
        {'first_name': 'Greg',
         'last_name': 'Gort'},
        {'first_name': 'Kanie',
         'last_name': 'West'}]

    companyThree_people = [
        {'first_name': 'Ken',
         'last_name': 'Barbie'},
        {'first_name': 'Low',
         'last_name': 'Temp'},
        {'first_name': 'Call',
         'last_name': 'Newman'}]
        
    companies = {'Company One': {'companies': companyOne_people},
                 'Company Two': {'companies': companyTwo_people},
                 'Company Three': {'companies': companyThree_people}}

    # iterate through company&persons data
    for company, company_data in companies.items():
        company = add_company(company)
        for person in company_data['companies']:
            add_person(company, person['first_name'], person['last_name'])

    # print the categories we have added
    for company in Company.objects.all():
        for person in Person.objects.filter(company=company):
            print(f'{company} - {person}')


def add_person(company, first_name, last_name):
    # person creation
    person = Person.objects.get_or_create(first_name=first_name, 
                                          last_name=last_name)[0]
    person.company=company
    person.save()
    return person

def add_company(company_name):
    # company creation
    company = Company.objects.get_or_create(company_name=company_name)[0]
    company.save()
    return company

if __name__ == '__main__':
    print('Start population script...')
    populate_db()
