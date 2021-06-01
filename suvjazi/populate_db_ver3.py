import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suvjazi.settings')
import django
django.setup()
from suvjazi_app.models import Company, Person, CompanyMembership
from suvjazi.settings import PROJECT_DIR
from random import randint
from faker import Faker


def populate_db():
    # adding persons
    for full_name in open(PROJECT_DIR / 'dummy_names_list.txt'):
        add_person(full_name)

    # adding companies
    for company_name in open(PROJECT_DIR / 'dummy_companies_list.txt'):
        company_name = ''.join(company_name.split())
        add_company(company_name)

    # adding connections between persons & companies
    for full_name in open(PROJECT_DIR / 'dummy_names_list.txt'):
        for company in open(PROJECT_DIR / 'dummy_companies_list.txt'):
            random_decider = randint(0, 1)
            if random_decider == 0:
                pass
            else:
                company_name = ''.join(company_name.split())
                date_joined = date_generator('join')
                date_leaved = date_generator('leave')
                add_connection(full_name, company_name, 
                               date_joined, date_leaved)


def date_generator(type_of_date):
    # generate test join date and test leave date
    if type_of_date == 'join':
        fake = Faker()
        return 

print(fake.date_between(start_date='-30y', end_date='today'))


def add_person(person_name):
    # person creation
    first_name = person_name.split()[0]
    last_name = person_name.split()[1]
    person = Person.objects.get_or_create(first_name=first_name, 
                                          last_name=last_name)[0]
    person.save()
    print(f'Person {person_name} created & saved')
    return person

def add_company(company_name):
    # company creation
    company = Company.objects.get_or_create(company_name=company_name)[0]
    company.save()
    print(f'Company {company_name} created & saved')
    return company

def add_connection(person_name, company_name, date_joined, date_leaved):
    # connection between person & company establishing
    company_membership = CompanyMembership.objects.get_or_create(
                                                        person=person_name,
                                                        company=company_name,
                                                        date_joined=date_joined,
                                                        date_leaved=date_leaved)
    company_membership.save()

