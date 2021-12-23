
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class AboutArea(blocks.StructBlock):
    about_title = blocks.CharBlock(required=True, max_length=100)
    about_subtitle = blocks.RichTextBlock(required=True)
    about_description = blocks.CharBlock(required=True, max_length=150)
    about_paragraph = blocks.RichTextBlock(required=True)
    about_button_url = blocks.URLBlock(required=False)
    about_button_page = blocks.PageChooserBlock(required=False)
    about_button_text = blocks.CharBlock(required=True, default='Learn More', max_length='50')
    about_image= ImageChooserBlock(required=False)

    class Meta:
        template = "streams/about_area.html"
        icon= 'placeholder'
        label='about area'

class Funfacts(blocks.StructBlock):
    fact = blocks.ListBlock(
        blocks.StructBlock(
                [
                    ("value",blocks.IntegerBlock()),
                    ("letter",blocks.CharBlock()),
                    ("title",blocks.TextBlock())
                ]
            )
        )

    class Meta:
        template = "streams/funfact.html"
        icon = 'placeholder'
        label = 'Funfacts'


class Featurearea(blocks.StructBlock):
    title = blocks.TextBlock(required=True)
    description = blocks.TextBlock(required=True)
    card = blocks.ListBlock(
        blocks.StructBlock(
        [   ("card_icon",blocks.TextBlock(required=True)),
            ("card_title",blocks.CharBlock()),
            ("card_desc",blocks.RichTextBlock())
        ])
    )    

    class Meta:
        template = "streams/Featurearea.html"
        


class Pricingsection(blocks.StructBlock):
    title = blocks.TextBlock(required=True)
    description = blocks.TextBlock(required=True)
    card = blocks.ListBlock(
        blocks.StructBlock(
        [   
            ("card_title",blocks.CharBlock()),
            ("price",blocks.CharBlock()),
            ("list",blocks.RichTextBlock()),
            ("button_url",blocks.URLBlock(required=False)),
            ("button_page",blocks.PageChooserBlock(required=False)),
            ("button_text",blocks.CharBlock(required=True, default='ChoosePlan', max_length='50')),


        ])
    )

    class Meta:
        template = "streams/pricing_area.html"
   
class Carousel(blocks.StructBlock):
    carousel = blocks.ListBlock(
        blocks.StructBlock(
            [
                
                ("description",blocks.TextBlock(required=True)),
                ("image", ImageChooserBlock(Required=False)),
                ("name", blocks.TextBlock()),
                ("role",blocks.TextBlock()),

            ]
        )
    )

    class Meta:
        template = "streams/carousel.html"


class RightImageLeftTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    heading = blocks.TextBlock()
    description = blocks.RichTextBlock()
    image = ImageChooserBlock()
    apps = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(Required=False)),
                ("button_url",blocks.URLBlock(required=False)),
                ("button_page",blocks.PageChooserBlock(required=False)),
                ("button_text",blocks.CharBlock(required=True, default='ChoosePlan', max_length='50')),

            ]
        )
    )

    class Meta:
        template = "streams/right_image_left_block.html"



class LeftImageRightTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    heading = blocks.TextBlock()
    description = blocks.RichTextBlock()
    image = ImageChooserBlock()
    apps = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(Required=False)),
                ("button_url",blocks.URLBlock(required=False)),
                ("button_page",blocks.PageChooserBlock(required=False)),
                ("button_text",blocks.CharBlock(required=True, default='ChoosePlan', max_length='50')),

            ]
        )
    )

    class Meta:
        template = "streams/left_image_right_block.html"


class BlogDetailBlock(blocks.StructBlock):
    title = blocks.RichTextBlock()
    blog = blocks.ListBlock(
        blocks.StructBlock(
            [
                
                ("name",blocks.TextBlock(required=False)),
                ("image", ImageChooserBlock(Required=False)),
                ("description", blocks.RichTextBlock()),
                ("date",blocks.DateBlock()),

            ]
        )
    )

    class Meta:
        template = 'streams/Image_with_title_Date.html'
        icon="edit"
        label='Blog Post'
