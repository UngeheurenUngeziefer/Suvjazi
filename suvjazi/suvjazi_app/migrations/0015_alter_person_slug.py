# Generated by Django 3.2.3 on 2021-06-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvjazi_app', '0014_alter_person_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(),
        ),
    ]