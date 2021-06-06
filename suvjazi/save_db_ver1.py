# script for saving data from django db

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suvjazi.settings')
import django
django.setup()
from suvjazi_app.models import Person, Company, CompanyMembership
import json


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
