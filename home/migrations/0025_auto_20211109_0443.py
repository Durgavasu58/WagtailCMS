# Generated by Django 3.2.9 on 2021-11-09 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0024_alter_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='button_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_text',
            field=models.CharField(default='Download', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_url',
            field=models.URLField(default='www.google.com'),
            preserve_default=False,
        ),
    ]