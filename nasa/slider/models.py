from django.db import models
from filer.fields.image import FilerImageField


class Slide(models.Model):
    image = FilerImageField(
        null=True, blank=True, related_name="slide_images", on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
