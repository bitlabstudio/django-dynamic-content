"""Admin classes for the dynamic_content app."""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from hvad.admin import TranslatableAdmin

from . import models


class DynamicContentAdmin(TranslatableAdmin):
    list_display = ['identifier', 'get_content', 'all_translations']
    search_fields = ['identifier', 'translations__content', ]

    def get_content(self, obj):
        return obj.content
    get_content.short_description = _('Content')

    def get_queryset(self, request):
        qs = super(DynamicContentAdmin, self).queryset(request)
        qs = qs.prefetch_related('translations')
        return qs

admin.site.register(models.DynamicContent, DynamicContentAdmin)
