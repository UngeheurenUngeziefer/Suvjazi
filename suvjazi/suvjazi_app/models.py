from django.db import models


# model for their job place
class Company(models.Model):
    company_name = models.CharField(max_length=128, unique=True)
    url = models.URLField()

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company_name


# model for humans
class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company = models.ManyToManyField(Company)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
