from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from streams import blocks



class BlogDetailPage(Page):

    template = "blog/blog-detail.html"    

    content = StreamField(
        [
            ("blog_detail", blocks.BlogDetailBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
       
        StreamFieldPanel("content"),
    ]
