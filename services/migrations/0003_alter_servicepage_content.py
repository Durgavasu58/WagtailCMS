# Generated by Django 3.2.9 on 2021-11-09 13:51

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_servicepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepage',
            name='content',
            field=wagtail.core.fields.StreamField([('service_details', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.RichTextBlock()), ('blog', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(Required=False)), ('description', wagtail.core.blocks.RichTextBlock()), ('date', wagtail.core.blocks.DateBlock())])))]))], blank=True, null=True),
        ),
    ]