# Generated by Django 4.1.13 on 2024-05-16 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Slide",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("order", models.PositiveIntegerField(default=0)),
                (
                    "image",
                    filer.fields.image.FilerImageField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="slide_images",
                        to=settings.FILER_IMAGE_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
    ]
