from django.db import models


class StatItem(models.Model):
    icon = models.ForeignKey("icons.Icon", on_delete=models.CASCADE)
    big_number = models.CharField(verbose_name="Número", max_length=255)
    title = models.CharField(verbose_name="Título", max_length=255)

    def __str__(self):
        return f"{self.big_number} {self.title}"

    class Meta:
        verbose_name = "Estatística"
        verbose_name_plural = "Estatísticas"
