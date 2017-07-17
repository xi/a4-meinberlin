from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore import fields
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore.models import Page
from wagtail.wagtailforms.models import AbstractEmailForm
from wagtail.wagtailforms.models import AbstractFormField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from apps.actions import blocks as actions_blocks

from . import blocks as cms_blocks
from . import emails


class SimplePage(Page):
    body = fields.RichTextField(blank=True)

    content_panels = [
        edit_handlers.FieldPanel('title'),
        edit_handlers.FieldPanel('body'),
    ]

    subpage_types = []


class HomePage(Page):
    body = fields.StreamField([
        ('paragraph', blocks.RichTextBlock(
            template='meinberlin_cms/blocks/richtext_block.html'
        )),
        ('call_to_action', cms_blocks.CallToActionBlock()),
        ('columns_text', cms_blocks.ColumnsBlock()),
        ('projects', cms_blocks.ProjectsWrapperBlock()),
        ('activities', actions_blocks.PlatformActivityBlock()),
    ])

    subtitle = models.CharField(max_length=120)

    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        edit_handlers.FieldPanel('subtitle'),
        ImageChooserPanel('header_image'),
        edit_handlers.StreamFieldPanel('body'),
    ]


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    link_page = models.ForeignKey('wagtailcore.Page')

    @property
    def url(self):
        return self.link_page.url

    def __str__(self):
        return self.title

    panels = [
        edit_handlers.FieldPanel('title'),
        edit_handlers.PageChooserPanel('link_page')
    ]


@register_snippet
class NavigationMenu(ClusterableModel):
    title = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title

    panels = [
        edit_handlers.FieldPanel('title'),
        edit_handlers.InlinePanel('items')
    ]


class NavigationMenuItem(Orderable, MenuItem):
    parent = ParentalKey('meinberlin_cms.NavigationMenu', related_name='items')


class EmailFormField(AbstractFormField):
    page = ParentalKey('EmailFormPage', related_name='form_fields')


class EmailFormPage(AbstractEmailForm):
    intro = fields.RichTextField(
        help_text='Introduction text shown above the form'
    )
    thank_you = fields.RichTextField(
        help_text='Text shown after form submission',
    )
    email_content = models.CharField(
        max_length=200,
        help_text='Email content message',
    )
    attach_as = models.CharField(
        max_length=3,
        choices=(
            ('xls', 'XLSX Document'),
            ('txt', 'Text'),
        ),
        default='xlsx',
        help_text='Form results are send in this document format',
    )

    content_panels = AbstractEmailForm.content_panels + [
        edit_handlers.MultiFieldPanel([
            edit_handlers.FieldPanel('intro', classname='full'),
            edit_handlers.FieldPanel('thank_you', classname='full'),
        ], 'Page'),
        edit_handlers.MultiFieldPanel([
            edit_handlers.FieldPanel('to_address'),
            edit_handlers.FieldPanel('subject'),
            edit_handlers.FieldPanel('email_content', classname='full'),
            edit_handlers.FieldPanel('attach_as'),
        ], 'Email'),
        edit_handlers.InlinePanel('form_fields', label='Form fields'),
    ]

    def send_mail(self, form):
        self.form = form
        if self.attach_as == 'xls':
            emails.XlsxFormEmail.send(self)
        elif self.attach_as == 'txt':
            emails.TextFormEmail.send(self)

    @property
    def field_values(self):
        fields = {}
        for field in self.form:
            value = field.value()
            if isinstance(value, list):
                value = ', '.join(value)
            fields[field.label] = value
        return fields
