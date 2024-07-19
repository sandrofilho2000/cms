from django.contrib import admin
from color_palette.models import ColorPalette
from django.utils.html import format_html


@admin.register(ColorPalette)
class ColorPaletteAdmin(admin.ModelAdmin):
    list_display = ["name", "main_color_preview"]

    def main_color_preview(self, obj):
        return format_html(
            '<div style="width: 24px; height: 24px; border-radius: 50%; background-color: {};"></div>',
            obj.main_color,
        )

    main_color_preview.short_description = "Cor principal"

    def main_bg_dark_preview(self, obj):
        return format_html(
            '<div style="width: 24px; height: 24px; border-radius: 50%; background-color: {};"></div>',
            obj.main_bg_dark,
        )

    main_bg_dark_preview.short_description = "Cor de fundo escura"
