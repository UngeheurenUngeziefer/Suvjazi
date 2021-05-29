from django import test
from django.test import TestCase
from suvjazi_app.models import Company, Person
from django.contrib.staticfiles import finders
from django.urls import reverse

class GeneralTests(TestCase):
    def test_serving_static_files(self):
        '''If using static files properly result is not 
           NONE once it finds image'''
        result = finders.find('images/test_logo.png')
        self.assertIsNotNone(result)

    def test_about_contain_image(self):
        '''check if is there an image on the about page'''
        response = self.client.get(reverse('about'))
        self.assertIn(b'img src="/media/', response.content)

    def test_about_using_templates(self):
        '''Check the template used to render index page'''
        about_response = self.client.get(reverse('about'))
        index_response = self.client.get(reverse('index'))
        self.assertTemplateUsed(index_response, 'suvjazi/index.html')
        self.assertTemplateUsed(about_response, 'suvjazi/about.html')


class CompanyMethodsTests(TestCase):
    def test_url_are_start_with_http(self):
        '''ensures company url starts with http'''
        test_company = Company(company_name='Test_Company', 
                          company_url='http://example.com')
        test_company.save()
        self.assertEqual((test_company.company_url[:4] == 'http'), True)

    # test for company/person existing


class PersonMethodsTest(TestCase):
    def test_name_without_numbers(self):
        '''checks if there numbers in first_name'''
        test_person = Person(first_name='Alex', last_name='Test')
        test_person.save()
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for i in numbers:
            self.assertNotIn(i, test_person.first_name, 'Number in first_name')
            self.assertNotIn(i, test_person.last_name, 'Number in last_name')

