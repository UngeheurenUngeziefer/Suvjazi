'''class able to save db from django app to JSON file
   class able to add specified number of persons and companies to db'''

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suvjazi.settings')
import django
django.setup()
from suvjazi_app.models import Company, Person, CompanyMembership
from random import randint
from faker import Faker
fake = Faker()
import json
from datetime import datetime


class DjangoDbManager():

    def __init__(self, option, num_of_persons=0, num_of_companies=0):
        self.num_of_persons = num_of_persons
        self.num_of_companies = num_of_companies
        self.option = option
        self.db_manager(self.option, self.num_of_persons, self.num_of_companies)


    def db_manager(self, option, num_of_persons, num_of_companies):
        '''function populating db with fake persons and companies
           or upload info from save_db JSON'''

        if option == 'fill_from_db':
            file = open('django_db.json')
            django_db_json = json.load(file)
            num_of_persons = 0
            num_of_companies = 0
            num_of_connections = 0

            for i in range(len(django_db_json['persons_fields']['first_name'])):
                # add persons
                first_name = django_db_json['persons_fields']['first_name'][i]
                last_name = django_db_json['persons_fields']['last_name'][i]
                full_name = first_name + ' ' + last_name
                self.add_person(full_name)
                num_of_persons += 1

            for i in range(len(django_db_json['company_fields']['company_name'])):
                # add companies
                company_name = django_db_json['company_fields']['company_name'][i]
                company_url = django_db_json['company_fields']['company_url'][i]
                self.add_company(company_name, company_url)
                num_of_companies += 1
            
            for i in range(len(django_db_json['company_membership_fields']
                                                                ['person_slug'])):
                # add connections between persons & companies
                datj = django_db_json['company_membership_fields']['date_joined'][i]
                datl = django_db_json['company_membership_fields']['date_leaved'][i]
                slug = django_db_json['company_membership_fields']['person_slug'][i]
                cnm = django_db_json['company_membership_fields']['company_name'][i]
                person = Person.objects.filter(slug=slug)[0]
                company = Company.objects.filter(company_name=cnm)[0]
                date_joined = datetime.strptime(datj, '%Y-%m-%d')
                date_leaved = datetime.strptime(datl, '%Y-%m-%d')
                self.add_connection(person, company, date_joined, date_leaved)
                num_of_connections += 1

            file.close()
            print('Info uploaded from django_db.json file!')
            print(f'Added {num_of_persons} new persons ' + \
                  f'& {num_of_companies} new companies ' + \
                  f'& {num_of_connections} connections between them.')

        elif option == 'fill_with_fakes':
            # adding persons
            for i in range(num_of_persons):
                self.add_person(fake.name())

            # adding companies
            for i in range(num_of_companies):
                self.add_company(fake.company(), fake.url())

            # adding connections between persons & companies
            for person in Person.objects.all():
                for company in Company.objects.all():
                    random_decider = randint(0, 2)
                    if random_decider == 0 or random_decider == 1:
                        pass
                    else:
                        date_joined, date_leaved = self.date_generator()
                        person = Person.objects.get(id=person.id)
                        company = Company.objects.get(
                                                company_name=company.company_name)
                        self.add_connection(person, company,
                                    date_joined, date_leaved)
            print(f'Added {num_of_persons} new persons ' + \
                f'& {num_of_companies} new companies')

        elif option == 'save_db':
            persons_dict = {'first_name': [], 'last_name': []}
            companies_dict = {'company_name': [], 'company_url': []}
            companies_memberships_dict = {'person_slug': [], 'company_name': [], 
                                        'date_joined': [], 'date_leaved': []}

            for person in Person.objects.all():
                persons_dict['first_name'].append(person.first_name)
                persons_dict['last_name'].append(person.last_name)

            for company in Company.objects.all():
                companies_dict['company_name'].append(company.company_name)
                companies_dict['company_url'].append(company.company_url)

            for company_membership in CompanyMembership.objects.all():
                companies_memberships_dict['person_slug'].append(
                                                        str(company_membership.person.slug))
                companies_memberships_dict['company_name'].append(
                                            str(company_membership.company.company_name))
                companies_memberships_dict['date_joined'].append(
                                                        str(company_membership.date_joined))
                companies_memberships_dict['date_leaved'].append(
                                                        str(company_membership.date_leaved))

            final_dict = {'persons_fields': persons_dict,
                        'company_fields': companies_dict,
                        'company_membership_fields': companies_memberships_dict}

            django_db_json = open('django_db.json', 'w')
            json.dump(final_dict, django_db_json)
            django_db_json.close()
            print('DB saved into django_db.json file!')

        elif option == 'purge_db':
            removed_persons_counter = 0
            removed_companies_counter = 0
            for person in Person.objects.all():
                person.delete()
                removed_persons_counter += 1

            for company in Company.objects.all():
                company.delete()
                removed_companies_counter += 1
            
            print('DB purged! ' + \
                 f'Deleted {removed_persons_counter} persons ' + \
                 f'& {removed_companies_counter} companies.')

        else:
            print('Given an unknown option!')


    def date_generator(self):
        # generate random join date and leave date
        a = fake.date()
        b = fake.date()

        if a > b:
            date_joined, date_leaved = b, a
        else:
            date_joined, date_leaved = a, b
        return date_joined, date_leaved


    def add_person(self, person_name):
        # person creation
        first_name = person_name.split()[0]
        last_name = person_name.split()[1]
        person = Person.objects.get_or_create(first_name=first_name, 
                                            last_name=last_name)[0]
        print(f'Person <{person_name}> created & saved')
        return person


    def add_company(self, company_name, company_url):
        # company creation
        company = Company.objects.get_or_create(company_name=company_name,
                                                company_url=company_url)[0]
        print(f'Company <{company_name}> created & saved')
        return company


    def add_connection(self, person, company, date_joined, date_leaved):
        # connection between person & company establishing
        
        company_membership = \
            CompanyMembership.objects.get_or_create(person=person,
                                                    company=company,
                                                    date_joined=date_joined,
                                                    date_leaved=date_leaved)[0]
        company_membership.save()
        print(f'Connection <{person.full_name}> - ' +
            f'<{company.company_name}> established & saved')


# options for manager: fill_from_db, fill_with_fakes n1 n2, save_db, purge_db
obj = DjangoDbManager('fill_from_db')
