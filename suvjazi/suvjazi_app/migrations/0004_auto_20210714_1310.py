# Generated by Django 3.2.3 on 2021-07-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvjazi_app', '0003_auto_20210627_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='co_authors',
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
