# Generated by Django 3.1.2 on 2020-10-26 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Suvjazi_app', '0019_remove_institute_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='category',
            new_name='institute',
        ),
    ]