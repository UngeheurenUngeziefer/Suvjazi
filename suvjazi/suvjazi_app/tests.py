from django.test import TestCase
from suvjazi_app.models import Company, Person, CompanyMembership
from django.contrib.staticfiles import finders
from django.urls import reverse
from populate_db_ver3 import add_person, add_company, date_generator
from faker import Faker
fake = Faker()

# add hook for autotests after push


class GeneralTests(TestCase):
        
    def test_serving_static_files(self):
        # test proper using of static files
        result = finders.find('images/test_logo.png')
        self.assertIsNotNone(result)
        

class IndexPageTests(TestCase):
    # tests for Index page

    def test_about_using_templates(self):
        # check the template used to render index page
        index_response = self.client.get(reverse('index'))
        self.assertTemplateUsed(index_response, 'suvjazi/index.html')

    def test_index_contains_word_suvjazi(self):
        # check if there is the word 'suvjazi' on index page
        response = self.client.get(reverse('index'))
        self.assertIn(b'Suvjazi', response.content)
    
    def test_index_has_title(self):
        # check to make sure that the title tag has been used
        response = self.client.get(reverse('index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


class AboutPageTests(TestCase):
    # tests for About page

    def test_about_using_templates(self):
        # check the template used to render about page
        about_response = self.client.get(reverse('about'))
        self.assertTemplateUsed(about_response, 'suvjazi/about.html')

    def test_about_contains_word_about(self):
        # check if there is the word 'suvjazi' on index page
        response = self.client.get(reverse('about'))
        self.assertIn(b'About', response.content)


class SuvjaziAppPageTests(TestCase):
    # tests for SuvjaziApp app

    def test_suvjazi_app_contains_word_suvjzai(self):
        # check if there is the word 'suvjazi app' on suvjazi_app page
        response = self.client.get(reverse('suvjazi_app'))
        self.assertIn(b'Suvjazi App', response.content)


class CompanyModelTests(TestCase):
    # tests for Company object

    def test_company_str(self):
        # checks if company_name returned in admin panel
        test_company = Company(company_name='Company_1')
        test_company.save()
        self.assertEqual(test_company.__str__(), 'Company_1')


class PersonModelTests(TestCase):
    # tests for Person object

    def create_fake_person(self):
        full_name = fake.name()
        first_name = full_name.split()[0]
        last_name = full_name.split()[1]
        test_person = Person(first_name=first_name, last_name=last_name)
        return test_person, full_name

    def test_persons_full_name(self):
        # checks if full_name created or not
        test_person, full_name = self.create_fake_person()
        self.assertEqual(test_person.full_name, full_name)

    def test_persons_str(self):
        # checks if full_name returned in admin panel
        test_person, full_name = self.create_fake_person()
        self.assertEqual(test_person.__str__(), full_name)

    def test_slug_name_resolver(self):
        # tests how same name persons resolver works
        full_name = fake.name()
        first_name = full_name.split()[0]
        last_name = full_name.split()[1]
        test_person = \
            Person.objects.create(first_name=first_name, last_name=last_name)
        same_name_person1 = \
            Person.objects.create(first_name=first_name, last_name=last_name)
        same_name_person2 = \
            Person.objects.create(first_name=first_name, last_name=last_name)
        same_name_person3 = \
            Person.objects.create(first_name=first_name, last_name=last_name)
        same_name_person4 = \
            Person.objects.create(first_name=first_name, last_name=last_name)
        same_name_person5 = \
            Person.objects.create(first_name=first_name, last_name=last_name)
        
        self.assertEqual(test_person.slug,
                        str(first_name + '-' + last_name).lower())
        self.assertEqual(same_name_person1.slug, 
                        str(first_name + '-' + last_name + '-' + '1').lower())
        self.assertEqual(same_name_person2.slug, 
                        str(first_name + '-' + last_name + '-' + '2').lower())
        self.assertEqual(same_name_person3.slug, 
                        str(first_name + '-' + last_name + '-' + '3').lower())
        self.assertEqual(same_name_person4.slug, 
                        str(first_name + '-' + last_name + '-' + '4').lower())
        self.assertEqual(same_name_person5.slug, 
                        str(first_name + '-' + last_name + '-' + '5').lower())    


class CompanyMembershipTests(TestCase):
    # tests for Company-Person objects relations

    def test_company_membership_str(self):
        '''checks if person_full_name-company_name 
        relation returned in admin panel'''
        
        person = add_person(fake.name())
        company = add_company(fake.company(), fake.url())
        date_joined, date_leaved = date_generator()

        test_company_membership = \
            CompanyMembership(person=person,
                              company=company,
                              date_joined=date_joined,
                              date_leaved=date_leaved)
        test_company_membership.save()
        nice_string = person.full_name + ' - ' + company.company_name

        self.assertEqual(test_company_membership.__str__(), nice_string)
