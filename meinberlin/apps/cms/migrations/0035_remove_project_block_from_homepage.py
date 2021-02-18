# Generated by Django 2.2.18 on 2021-02-18 10:01

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('meinberlin_cms', '0034_emailformfield_clean_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(template='meinberlin_cms/blocks/richtext_block.html')), ('call_to_action', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50))])), ('image_call_to_action', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=80)), ('body', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50))])), ('columns_text', wagtail.core.blocks.StructBlock([('columns_count', wagtail.core.blocks.ChoiceBlock(choices=[(2, 'Two columns'), (3, 'Three columns'), (4, 'Four columns')])), ('columns', wagtail.core.blocks.ListBlock(wagtail.core.blocks.RichTextBlock(label='Column body')))])), ('activities', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(label='Heading')), ('count', wagtail.core.blocks.IntegerBlock(default=5, label='Count'))])), ('accordion', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=False))])), ('infographic', wagtail.core.blocks.StructBlock([('text_left', wagtail.core.blocks.CharBlock(max_length=50)), ('text_center', wagtail.core.blocks.CharBlock(max_length=50)), ('text_right', wagtail.core.blocks.CharBlock(max_length=50))])), ('map_teaser', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('body', wagtail.core.blocks.RichTextBlock())]))]),
        ),
    ]
