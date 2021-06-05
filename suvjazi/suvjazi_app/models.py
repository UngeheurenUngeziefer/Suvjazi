from django.db import models
from django.template.defaultfilters import slugify


class Person(models.Model):
    # model for humans
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    slug = models.SlugField()

    def slug_same_name_resolver(self, correct_slug, counter):
        '''resolve same full_name of Person's conflicts 
           by adding number after name in slug'''

        if len(Person.objects.filter(slug=correct_slug)) == 0:
            if counter == 0:
                self.slug = correct_slug
                print('Slug successfully added!')
            else:
                self.slug = correct_slug
                print('Person have namesake in db. ' +
                      f'{counter} added to the end of slug!')

        elif len(Person.objects.filter(slug=correct_slug)) == 1:
            if counter == 0:
                counter += 1
                correct_slug = correct_slug + '-' + str(counter)
                self.slug_same_name_resolver(correct_slug, counter)
            else:
                counter += 1
                correct_slug = correct_slug[:-2]
                correct_slug = correct_slug + '-' + str(counter)
                self.slug_same_name_resolver(correct_slug, counter)

    def save(self, *args, **kwargs):
        # creates slug link for every Person object & automaticly save obj
        correct_slug = f'{self.first_name.lower()}-{self.last_name.lower()}'
        counter = 0
        self.slug_same_name_resolver(correct_slug, counter)
        super(Person, self).save(*args, **kwargs)

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
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        # creates slug link for every Company object & automaticly save obj
        self.slug = slugify(self.company_name)
        super(Company, self).save(*args, **kwargs)

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
