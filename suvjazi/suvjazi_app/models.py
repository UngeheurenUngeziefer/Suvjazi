from django.db import models


class Company(models.Model):
    # model for companies
    company_name = models.CharField(max_length=128, unique=True)
    company_url = models.URLField()

    class Meta:
        # to show correct plural in admin panel
        verbose_name_plural = 'Companies'

    def __str__(self):
        # to show company name in console
        return self.company_name

    
class Person(models.Model):
    # model for humans
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company = models.ManyToManyField(Company)

    @property
    def full_name(self):
        # function to show persons full name in admin panel table
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        # to show full name in console
        return self.first_name + ' ' + self.last_name
