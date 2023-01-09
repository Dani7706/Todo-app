from django.contrib import admin

from devsearch.reviews.models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=['value','project_id']
