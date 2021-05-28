from django.db import models


class Company(models.Model):
    # model for companies
    company_name = models.CharField(max_length=128, unique=True)
    company_url = models.URLField()

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company_name


class Person(models.Model):
    # model for humans
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company = models.ManyToManyField(Company)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
