from suvjazi.settings import PROJECT_DIR
from django import test
from django.test import TestCase
from suvjazi_app.models import Company, Person
from django.contrib.staticfiles import finders
from django.urls import reverse
from populate_db import populate_db


class GeneralTests(TestCase):
    
    def test_serving_static_files(self):
        # test proper using of static files
        result = finders.find('images/test_logo.png')
        self.assertIsNotNone(result)

    def test_about_contain_image(self):
        # check if is there an image on the about page
        response = self.client.get(reverse('about'))
        self.assertIn(b'img src="/media/', response.content)


class IndexPageTests(TestCase):
    
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

    def test_about_using_templates(self):
        # check the template used to render about page
        about_response = self.client.get(reverse('about'))
        self.assertTemplateUsed(about_response, 'suvjazi/about.html')

    def test_about_contains_word_about(self):
        # check if there is the word 'suvjazi' on index page
        response = self.client.get(reverse('about'))
        self.assertIn(b'About', response.content)


class SuvjaziAppPageTests(TestCase):

    def test_suvjazi_app_contains_word_suvjzai(self):
        # check if there is the word 'suvjazi' on index page
        response = self.client.get(reverse('suvjazi_app'))
        self.assertIn(b'Suvjazi app', response.content)


class CompanyModelTests(TestCase):

    def test_url_are_starts_with_http(self):
        # ensures company url starts with http
        test_company = Company(company_name='Test Company', 
                          company_url='http://example.com')
        test_company.save()
        self.assertEqual((test_company.company_url[:4] == 'http'), True)

    def test_company_name_field(self):
        # ensures that company_name saved properly
        test_company = Company(company_name='Test Company')
        test_company.save()
        self.assertEqual(type(test_company.company_name), type('Test Company'))

    def setUp(self):
        # method run populate_db script for tests
        try:
            populate_db()
        except ImportError:
            print('The module populate_db does not exist')
        except NameError:
            print('The function populate_db() does not exist or is not correct')
        except:
            print('Something went wrong in the populate_db() function')

    def get_company(self, company_name):
        # method returns None or Company obj by company_name
        try:                  
            company = Company.objects.get(company_name=company_name)
        except Company.DoesNotExist:
            company = None
        return company
        
    def test_company_added(self):
        # checks is all companies from dummy_list added by population script 
        for company_name in open(PROJECT_DIR / 
                                        'dummy_companies_list.txt'):
            company_name = ''.join(company_name.split())
            company = self.get_company(company_name=company_name)
            self.assertIsNotNone(company)


class PersonModelTest(TestCase):
    
    def test_name_without_numbers(self):
        # checks if there numbers in first_name
        test_person = Person(first_name='Alex', last_name='Test')
        test_person.save()
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for i in numbers:
            self.assertNotIn(i, test_person.first_name, 'Number in first_name')
            self.assertNotIn(i, test_person.last_name, 'Number in last_name')

    def setUp(self):
        # method run populate_db script for tests
        try:
            populate_db()
        except ImportError:
            print('The module populate_db does not exist')
        except NameError:
            print('The function populate_db() does not exist or is not correct')
        except:
            print('Something went wrong in the populate_db() function')

    def get_person(self, first_name, last_name):
        # method returns None or Person obj by f_name and l_name
        try:                  
            person = Person.objects.get(first_name=first_name,
                                        last_name=last_name)
        except Person.DoesNotExist:    
            person = None
        return person
        
    def test_persons_added(self):
        # checks is all persons from dummy_list added by population script 
        for full_name in open(PROJECT_DIR / 'dummy_names_list.txt'):
            first_name = full_name.split()[0]
            last_name = full_name.split()[1]
            person = self.get_person(first_name=first_name,
                                    last_name=last_name)  
            self.assertIsNotNone(person)

    def test_persons_full_name(self):
        # checks if full_name created or not
        test_person = Person(first_name='Alex', last_name='Test')
        test_person.save()
        self.assertEqual(test_person.full_name, 'Alex Test')
