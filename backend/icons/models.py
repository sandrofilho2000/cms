from django.db import models


class Icon(models.Model):
    name = models.CharField(max_length=255, default="ícone", verbose_name="Nome")
    code = models.TextField(verbose_name="Código SVG")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ícone"
        verbose_name_plural = "Ícones"
