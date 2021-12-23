from django.db import models

from wagtail.core.models import Page
from  wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from streams import blocks



class ServicePage(Page):
    template = "services/services.html"

    content = StreamField(
        [
            ("service_details", blocks.BlogDetailBlock()),
            ("pricing_section",blocks.Pricingsection()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
       
        StreamFieldPanel("content"),
        
    ]

