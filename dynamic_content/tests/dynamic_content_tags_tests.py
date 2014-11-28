"""Tests for the templatetags of the dynamic_content app."""
from django.test import TestCase

from ..templatetags import dynamic_content_tags as tags


class GetContentTestCase(TestCase):
    """Tests for the ``get_content`` assignment tag."""
    longMessage = True

    def test_tag(self):
        result = tags.get_content('foobar')
        self.assertTrue(result.pk, msg=(
            'Should create a new `DynamicContent` instance'))

        result2 = tags.get_content('foobar')
        self.assertEqual(result2.pk, result.pk, msg=(
            'Should return the existing `DynamicContent` instance'))
