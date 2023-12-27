from django.contrib import admin

from links.models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'link',
        'hash_code',
        'user',
    )
    list_filter = (
        'user',
        'id',
    )
    search_fields = (
        'user',
        'id',
    )