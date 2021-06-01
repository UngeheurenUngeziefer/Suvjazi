from django.db import models


class Person(models.Model):
    # model for humans
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    @property
    def full_name(self):
        # function to show persons full name in admin panel table
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        # to show full name in console
        return self.first_name + ' ' + self.last_name


class Company(models.Model):
    # model for companies
    company_name = models.CharField(max_length=128, unique=True)
    company_url = models.URLField()
    person = models.ManyToManyField(Person, through='CompanyMembership')

    class Meta:
        # to show correct plural in admin panel
        verbose_name_plural = 'Companies'

    def __str__(self):
        # to show company name in console
        return self.company_name


class CompanyMembership(models.Model):
    # class to connect Person and Company many-to-many relation
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_leaved = models.DateField()
    job_functions_description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'CompanyMemberships'

    def __str__(self):
        # method to show connections between Person and Company in admin panel
        return self.person.full_name + ' - ' + self.company.company_name
