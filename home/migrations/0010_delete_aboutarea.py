# Generated by Django 3.2.9 on 2021-11-07 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0009_aboutarea'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutArea',
        ),
    ]
