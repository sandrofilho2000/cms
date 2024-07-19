from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(
        max_length=255,
        default="Kickstart your Next.js 14 website in minutes",
        null=False,
        verbose_name="Título",
    )
    highlight_word = models.CharField(
        max_length=255,
        default="Next.js 14",
        null=False,
        verbose_name="Palavra destacada do título",
    )
    text = models.CharField(
        max_length=255,
        default="Inators UI is a collection of UI components and templates based on Tailwind and Shadcn/ui, just copy and use",
        null=False,
        verbose_name="Texto da hero",
    )

    command_line = models.CharField(
        max_length=255,
        null=False,
        verbose_name="Comando",
        default="npx shadcn-ui@latest init",
    )

    cta_text = models.CharField(
        max_length=255, verbose_name="Texto do CTA", default="Browse all Components"
    )
    cta_link = models.CharField(max_length=255, verbose_name="Link do CTA", default="#")
    img = models.FileField(upload_to="", null=True)

    class Meta:
        verbose_name = "Sessão Hero"
        verbose_name_plural = "Sessões Hero"

    def __str__(self):
        return self.title
