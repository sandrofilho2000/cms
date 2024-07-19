from os import name
from tabnanny import verbose
from django.db import models
import uuid

from features.models import Feature
from stats.models import StatItem


class WebsiteVersions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nome da variante")
    color_palette = models.ForeignKey(
        "color_palette.ColorPalette",
        verbose_name="Paleta de cores",
        on_delete=models.CASCADE,
        default=0,
    )
    active = models.BooleanField(default=True)
    hero = models.ForeignKey(
        "hero.Hero",
        verbose_name="Sessão Hero",
        on_delete=models.CASCADE,
        default=0,
    )

    stats = models.ManyToManyField(StatItem)
    features = models.ManyToManyField(Feature)
    banner = models.ForeignKey(
        "banners.Banner",
        verbose_name="Banner",
        on_delete=models.CASCADE,
    )

    faq = models.ForeignKey(
        "faq.Faq",
        verbose_name="Perguntas e respostas",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Variante"
        verbose_name_plural = "Variantes do site"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.active and not self.pk:
            WebsiteVersions.objects.filter(active=True).update(active=False)
        elif self.active and self.pk:
            WebsiteVersions.objects.exclude(pk=self.pk).filter(active=True).update(
                active=False
            )

        super().save(*args, **kwargs)
