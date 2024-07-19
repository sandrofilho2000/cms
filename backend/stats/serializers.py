from rest_framework import serializers
from stats.models import StatItem


class StatItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatItem
        fields = ["icon", "big_number", "title"]
