"""Models for the dynamic_content app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from hvad.models import TranslatableModel, TranslatedFields, TranslationManager


class DynamicContent(TranslatableModel):
    """
    Holds dynamic content that admins can manipulate via the Django admin.

    :identifier: Unique identifier. To be used in templates with the
      ``render_content`` templatetag.
    :content: Multilingual text. The content to be displayed.

    """
    identifier = models.CharField(
        max_length=256,
        verbose_name=('Unique identifier'),
    )

    translations = TranslatedFields(
        content=models.TextField(
            verbose_name=_('Content'),
        )
    )

    objects = TranslationManager()
