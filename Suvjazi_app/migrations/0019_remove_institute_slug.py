# Generated by Django 3.1.2 on 2020-10-26 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Suvjazi_app', '0018_person_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institute',
            name='slug',
        ),
    ]
