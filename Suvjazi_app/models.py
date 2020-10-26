from django.db import models
from django.urls import reverse
from datetime import date
from pytils.translit import slugify

class Institute(models.Model):
	title = models.CharField(max_length=255, default='')
	slug = models.SlugField(blank=True, default='')
	description = models.TextField(default='')

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Institute, self).save()

	def get_absolute_url(self):
		return reverse('institute_detail', args=[str(self.slug)])

class Person(models.Model):
	name = models.CharField(max_length=100, default='')
	slug = models.SlugField(blank=True, default='')
	# birthday = models.DateField()
	# age = date.today() - birthday
	description = models.TextField(default='')
	institute = models.ForeignKey(Institute, null=True,
	 on_delete=models.PROTECT)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Person, self).save()

	def get_absolute_url(self):
		return reverse('person_detail', args=[str(self.slug)])