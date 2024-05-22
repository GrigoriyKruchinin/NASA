from django.db import models
from filer.fields.image import FilerImageField
from django.utils.translation import gettext_lazy as _


class Slide(models.Model):
    image = FilerImageField(
        null=True,
        blank=True,
        related_name="slide_images",
        on_delete=models.SET_NULL,
        verbose_name=_("Image"),
    )
    title = models.CharField(
        max_length=100,
        verbose_name=_("Title"),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name=_("Order"),
    )

    class Meta:
        verbose_name = _("Slide")
        verbose_name_plural = _("Slides")
        ordering = ["order"]

    def __str__(self):
        return self.title
