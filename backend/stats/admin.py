from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from stats.models import StatItem


@admin.register(StatItem)
class StatItemAdmin(admin.ModelAdmin):
    list_display = ["big_number", "title", "icon_preview"]

    def icon_preview(self, obj):
        return format_html(
            """<div style="display: flex; align-items: center; gap: 4px; font-size: 25px;">
                {}
            </div>""",
            mark_safe(obj.icon.code),
        )

    icon_preview.short_description = "ícone"
