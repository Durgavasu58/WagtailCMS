# Generated by Django 3.2.9 on 2021-11-09 13:50

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='content',
            field=wagtail.core.fields.StreamField([('service_details', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.RichTextBlock()), ('blog', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.TextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(Required=False)), ('description', wagtail.core.blocks.RichTextBlock()), ('date', wagtail.core.blocks.DateBlock())])))]))], blank=True, null=True),
        ),
    ]