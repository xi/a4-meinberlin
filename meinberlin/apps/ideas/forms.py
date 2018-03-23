from django import forms
from django.utils.translation import ugettext_lazy as _

from adhocracy4.categories.forms import CategorizableFieldMixin

from . import models


class IdeaForm(CategorizableFieldMixin, forms.ModelForm):
    right_of_use = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.image:
            self.initial['right_of_use'] = True

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        right_of_use = cleaned_data.get('right_of_use')
        if image and not right_of_use:
            self.add_error('right_of_use',
                           _("You want to upload an image. "
                             "Please check that you have the "
                             "right of use for the image."))

    class Meta:
        model = models.Idea
        fields = ['name', 'description', 'image', 'category']


class IdeaModerateForm(forms.ModelForm):
    class Meta:
        model = models.Idea
        fields = ['moderator_feedback']
