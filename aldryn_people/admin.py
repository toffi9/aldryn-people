# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from parler.admin import TranslatableAdmin
from aldryn_translation_tools.admin import AllTranslationsMixin
# We are using VersionedPlaceholderAdminMixin because atm (0.1.0)
# it also contains important methods and changes to provide
# translations support in revisions. Be aware that this might
# be changed in further releases.
from aldryn_reversion.admin import VersionedPlaceholderAdminMixin

from .models import Person, Group
from .forms import PersonForm


class PersonAdmin(VersionedPlaceholderAdminMixin,
                  AllTranslationsMixin,
                  TranslatableAdmin):

    list_display = [
        '__str__', 'email', 'vcard_enabled', ]
    list_filter = ['groups', 'vcard_enabled']
    search_fields = ('name', 'email', 'translations__function')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('user',)

    fieldsets = (
        (None, {
            'fields': (
                'name', 'function', 'slug', 'visual', 'vcard_enabled'
            ),
        }),
        (_('Contact'), {
            'fields': (
                'phone', 'mobile', 'fax', 'email', 'website', 'user'
            ),
        }),
        (None, {
            'fields': (
                'groups', 'description',
            ),
        }),
    )

    form = PersonForm


class GroupAdmin(VersionedPlaceholderAdminMixin,
                 AllTranslationsMixin,
                 TranslatableAdmin):

    list_display = ['__str__', 'city', ]
    search_filter = ['name']

    fieldsets = (
        (None, {
            'fields': (
                'name', 'description', 'phone', 'fax', 'email', 'website'
            ),
        }),
        (_('Address'), {
            'fields': (
                'address', 'postal_code', 'city'
            ),
        }),
    )

admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
