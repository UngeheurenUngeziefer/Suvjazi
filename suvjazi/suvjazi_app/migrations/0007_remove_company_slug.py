# Generated by Django 3.2.3 on 2021-05-29 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suvjazi_app', '0006_company_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='slug',
        ),
    ]