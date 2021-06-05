import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suvjazi.settings')
import django
django.setup()
from suvjazi_app.models import Company, Person, CompanyMembership
# from suvjazi.settings import PROJECT_DIR
from random import randint
from faker import Faker
fake = Faker()


def populate_db(num_of_persons, num_of_companies):
    # function populating db with fake persons and companies

    # adding persons
    for i in range(num_of_persons):
        add_person(fake.name())

    # adding companies
    for i in range(num_of_companies):
        add_company(fake.company(), fake.url())

    # adding connections between persons & companies
    for person in Person.objects.all():
        for company in Company.objects.all():
            random_decider = randint(0, 1)
            if random_decider == 0:
                pass
            else:
                date_joined, date_leaved = date_generator()
                person = Person.objects.get(id=person.id)
                company = Company.objects.get(company_name=company.company_name)
                add_connection(person, company,
                               date_joined, date_leaved)


def date_generator():
    # generate random join date and leave date
    a = fake.date()
    b = fake.date()

    if a > b:
        date_joined, date_leaved = b, a
    else:
        date_joined, date_leaved = a, b
    return date_joined, date_leaved


def add_person(person_name):
    # person creation
    first_name = person_name.split()[0]
    last_name = person_name.split()[1]
    person = Person.objects.get_or_create(first_name=first_name, 
                                          last_name=last_name)[0]
    print(f'Person <{person_name}> created & saved')
    return person


def add_company(company_name, company_url):
    # company creation
    company = Company.objects.get_or_create(company_name=company_name,
                                            company_url=company_url)[0]
    print(f'Company <{company_name}> created & saved')
    return company


def add_connection(person, company, date_joined, date_leaved):
    # connection between person & company establishing
    
    company_membership = \
        CompanyMembership.objects.get_or_create(person=person,
                                                company=company,
                                                date_joined=date_joined,
                                                date_leaved=date_leaved)[0]
    company_membership.save()
    print(f'Connection <{person.full_name}> - ' +
          f'<{company.company_name}> established & saved')


if __name__ == '__main__':
    print('Start populating DB...') # pragma: no cover
    populate_db(50, 10)             # pragma: no cover
