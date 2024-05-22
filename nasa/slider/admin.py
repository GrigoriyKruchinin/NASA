from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from django.utils.translation import gettext_lazy as _
from easy_thumbnails.files import get_thumbnailer
from .models import Slide


@admin.register(Slide)
class SlideAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "display_thumbnail")
    ordering = ["order"]

    def display_thumbnail(self, obj):
        if obj.image:
            thumbnail_options = {"size": (100, 100), "crop": True}
            thumbnail_url = (
                get_thumbnailer(obj.image).get_thumbnail(thumbnail_options).url
            )
            return format_html('<img src="{}" />', thumbnail_url)
        else:
            return _("No image")

    display_thumbnail.allow_tags = True
    display_thumbnail.short_description = _("Image")
