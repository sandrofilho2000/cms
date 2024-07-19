from django.contrib import admin
from django.utils.html import format_html

from features.models import Feature


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ["title", "img_preview", "subtitle"]

    def img_preview(self, obj):
        return format_html(
            """<a style="display: flex; align-items: center; gap: 4px" href="http://localhost:8000/media/{}" target="_blank">
                <img style='width: 50px; height: 24px; border-radius: 2px; ' src='http://localhost:8000/media/{}'/>
            </a>""",
            obj.img,
            obj.img,
        )

    img_preview.short_description = "Imagem"
