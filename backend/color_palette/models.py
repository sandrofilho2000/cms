from tabnanny import verbose
from django.db import models
from colorfield.fields import ColorField


class ColorPalette(models.Model):
    name = models.CharField(max_length=255)
    main_color = ColorField(null=False, verbose_name="Cor principal", default="#e11d48")

    class Meta:
        verbose_name = "Paleta de cores"
        verbose_name_plural = "Paleta de cores"

    def __str__(self):
        return self.name
