"""Templatetags for the dynamic_content app."""
from django import template

from .. import models


register = template.Library()


@register.simple_tag
def get_content(identifier, default=None):
    '''
    Returns the DynamicContent instance for the given identifier.

    If no object is found, a new one will be created.

    :param identifier: String representing the unique identifier of a
      ``DynamicContent`` object.
    :param default: String that should be used in case that no matching
      ``DynamicContent`` object exists.

    '''
    if default is None:
        default = ''

    try:
        return models.DynamicContent.objects.get(identifier=identifier)
    except models.DynamicContent.DoesNotExist:
        return models.DynamicContent.objects.create(
            identifier=identifier, content=default)
