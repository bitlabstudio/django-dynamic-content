"""Models for the dynamic_content app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from parler.managers import TranslatableManager
from parler.models import TranslatableModel, TranslatedFields


class DynamicContent(TranslatableModel):
    """
    Holds dynamic content that admins can manipulate via the Django admin.

    :identifier: Unique identifier. To be used in templates with the
      ``render_content`` templatetag.
    :content: Multilingual text. The content to be displayed.

    """
    identifier = models.CharField(
        unique=True,
        max_length=256,
        verbose_name=('Unique identifier'),
    )

    translations = TranslatedFields(
        content=models.TextField(
            verbose_name=_('Content'),
            blank=True,
        ),
        content_html=RichTextField(
            verbose_name=_('Content (html)'),
            blank=True,
        ),
    )

    objects = TranslatableManager()
