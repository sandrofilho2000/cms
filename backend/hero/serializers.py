from hero.models import Hero
from rest_framework import serializers


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"
