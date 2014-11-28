"""Tests for the models of the dynamic_content app."""
from django.test import TestCase

from .. import models


class DynamicContentTestCase(TestCase):
    """Tests for the ``DynamicContent`` model."""
    def test_model(self):
        obj = models.DynamicContent.objects.create(
            identifier='foobar', content='barfoo')
        self.assertTrue(obj.pk)
