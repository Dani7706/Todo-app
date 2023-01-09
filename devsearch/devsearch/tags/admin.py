from django.contrib import admin

from devsearch.tags.models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name']
