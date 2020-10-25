from django.db import models

class Institute(models.Model):
	title = models.CharField(max_length=255, default='')
	description = models.TextField(default='')
	image = models.ImageField(upload_to='Suvjazi_app/media/images/institutes/',
	 default='media/institutes/default.jpg')

	def __str__(self):
		return self.title
