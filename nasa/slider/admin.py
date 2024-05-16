from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from .models import Slide


@admin.register(Slide)
class SlideAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "display_image")
    ordering = ["order"]

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:100px;max-height:100px" />',
                obj.image.url,
            )
        else:
            return "No image"

    display_image.allow_tags = True
    display_image.short_description = "Image"
