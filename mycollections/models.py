from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    subject = models.CharField(max_length=300, blank=True)
    owner = models.CharField(max_length=300, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)


class CollectionTitle(models.Model):
    """
    A Class for Collection titles.

    """
    collection = models.ForeignKey(Collection,
        related_name="has_titles", on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name="Title")
    

    def __str__(self):
        return str(self.name)


class Membership(models.Model):
    company = models.ForeignKey(CollectionTitle,
        related_name="has_company", on_delete=models.CASCADE)
    person = models.ForeignKey(Collection,
        related_name="person", on_delete=models.CASCADE)
    date_joined = models.DateField()
    salary = models.CharField(max_length=50)

    def __str__(self):
        return str(self.company.name)

