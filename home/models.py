from django.db import models

from wagtail.core.models import Page
from  wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from streams import blocks


class HomePage(Page):
    
    template = 'home/home_page.html'

    body = StreamField(
        [
            ("about_area",blocks.AboutArea()),
            ("fun_facts",blocks.Funfacts()),
            ("features_Area",blocks.Featurearea()),
            ("carousel",blocks.Carousel()),
            ("pricing_section",blocks.Pricingsection()),
            ("Leftimagerightblock",blocks.LeftImageRightTextBlock()),
            ("Rightimagerightblock",blocks.RightImageLeftTextBlock()),   

        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
       
        StreamFieldPanel('body'),

    ]
