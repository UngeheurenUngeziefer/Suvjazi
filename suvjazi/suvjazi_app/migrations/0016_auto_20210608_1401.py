# Generated by Django 3.2.3 on 2021-06-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvjazi_app', '0015_alter_person_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymembership',
            name='date_joined',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='companymembership',
            name='date_leaved',
            field=models.DateField(null=True),
        ),
    ]
