from django.contrib import admin
from hero.models import Hero
from django.utils.html import format_html


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "title",
        "img_preview",
        "command_line",
        "cta_text",
        "cta_link",
    )

    def img_preview(self, obj):
        return format_html(
            """<a style="display: flex; align-items: center; gap: 4px" href="http://localhost:8000/media/{}" target="_blank">
                <img style='width: 50px; height: 24px; border-radius: 2px; ' src='http://localhost:8000/media/{}'/>
            </a>""",
            obj.img,
            obj.img,
        )

    img_preview.short_description = "Imagem"
