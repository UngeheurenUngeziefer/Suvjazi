import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'suvjazi.settings')

import django
django.setup()

from suvjazi_app.models import Company, Person

def populate_db():
    # function to populate django app db
    person1 = [
        {'company_name': 'Company_1',
         'url': 'http://example.com'},
        {'company_name': 'Company_2',
         'url': 'http://example2.com'}
        ]

    person2 = [
        {'company_name': 'Company_2',
         'url': 'http://example2.com'},
        {'company_name': 'Company_3',
         'url': 'http://example3.com'}
        ]

    person3 = [
        {'company_name': 'Company_1',
         'url': 'http://example.com'},
        {'company_name': 'Company_2',
         'url': 'http://example2.com'},
        {'company_name': 'Company_4',
         'url': 'http://example3.com'}
        ]

    person4 = [
        {'company_name': 'Company_5',
         'url': 'http://example5.com'}
        ]
    
    person5 = [
        {'company_name': 'Company_1',
         'url': 'http://example1.com'}, 
        {'company_name': 'Company_5',
         'url': 'http://example5.com'} 
        ]

    persons = {'Annie Krotova': {'persons': person1},
               'Eminem Marshall': {'persons': person2},
               'Evanessence Smith': {'persons': person3},
               'Ivan Ivanov': {'persons': person4},
               'Amir Hadjatin': {'persons': person1},
               'Greg Stivenson': {'persons': person2},
               'Anna Vasileko': {'persons': person3},
               'Call Newman': {'persons': person4},
               'Low Temp': {'persons': person5},
               'Ken Barbie': {'persons': person1},
               'Kanie West': {'persons': person2},
               'Greg Gort': {'persons': person3},
               'Kristina Alova': {'persons': person4},
               'Ellie Stockholm': {'persons': person5},
               'Anna Smith': {'persons': person1},
               'Oleg Devyatov': {'persons': person2}}


    # iterate through company&persons data
    for person, person_data in persons.items():
        person = add_person(person)
        for company in person_data['persons']:
            add_company(company['company_name'], company['url'], person)

    
    # print the companies we have added
    for person in Person.objects.all():
        for company in Company.objects.filter(person=person):
            print(f'{person} - {company}')


def add_company(company_name, company_url, person):
    # company creation
    company = Company.objects.get_or_create(company_name=company_name)[0]
    company.url = company_url
    company.save()
    person.company.add(company)

    return company


def add_person(person_name):
    # person creation
    first_name = person_name.split()[0]
    last_name = person_name.split()[1]

    person = Person.objects.get_or_create(first_name=first_name, 
                                          last_name=last_name)[0]
    person.save()
    return person

   


if __name__ == '__main__':
    print('Start populating DB...')
    populate_db()