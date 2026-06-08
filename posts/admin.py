from django.contrib import admin
from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'source', 'created_at', 'text_preview']
    list_filter = ['source', 'tags']
    search_fields = ['author', 'text']
    filter_horizontal = ['tags']

    def text_preview(self, obj):
        return obj.text[:80]
    text_preview.short_description = 'Texto'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
