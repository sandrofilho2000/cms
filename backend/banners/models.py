from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título")
    subtitle = models.CharField(max_length=255, verbose_name="Subtítulo")
    cta_text = models.CharField(max_length=255, verbose_name="Texto do botão")
    cta_link = models.CharField(
        max_length=255, verbose_name="Link do botão", default="#"
    )

    def __str__(self):
        return self.title
