from color_palette.models import ColorPalette
from rest_framework import serializers


class ColorPaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorPalette
        fields = ("name", "main_color")
