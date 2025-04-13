from django.contrib import admin
from website_versions.models import WebsiteVersions
from django.utils.html import format_html


@admin.register(WebsiteVersions)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "hero_title",
        "img_preview",
        "link_preview",
        "main_color_preview",
        "active",
    ]
    list_display_links = [
        "name",
    ]
    list_editable = [
        "active",
    ]

    def main_color_preview(self, obj):
        return format_html(
            """<div style="display: flex; align-items: center; gap: 4px">
                <div style='width: 24px; height: 24px; border-radius: 50%; background-color: {};'></div>
                <span>{}</span>
            </div>""",
            obj.color,
            obj.color,
        )

    main_color_preview.short_description = "Cor principal"

    def img_preview(self, obj):
        return format_html(
            """<a style="display: flex; align-items: center; gap: 4px" href="http://localhost:8000/media/{}" target="_blank">
                <img style='width: 50px; height: 24px; border-radius: 2px; ' src='http://localhost:8000/media/{}'/>
            </a>""",
            obj.hero.img,
            obj.hero.img,
        )

    img_preview.short_description = "Imagem"

    def link_preview(self, obj):
        return format_html(
            """<a style="display: flex; align-items: center; gap: 4px" href="http://localhost:3000/lid/{}" target="_blank">
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 576 512" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M572.52 241.4C518.29 135.59 410.93 64 288 64S57.68 135.64 3.48 241.41a32.35 32.35 0 0 0 0 29.19C57.71 376.41 165.07 448 288 448s230.32-71.64 284.52-177.41a32.35 32.35 0 0 0 0-29.19zM288 400a144 144 0 1 1 144-144 143.93 143.93 0 0 1-144 144zm0-240a95.31 95.31 0 0 0-25.31 3.79 47.85 47.85 0 0 1-66.9 66.9A95.78 95.78 0 1 0 288 160z"></path></svg>
                Prévia 
            </a>""",
            obj.pk,
        )

    link_preview.short_description = "Prévia da variante"

    def hero_title(self, obj):
        return obj.hero.title

    hero_title.short_description = "Título"
