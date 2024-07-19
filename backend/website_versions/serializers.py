from stats.models import StatItem
from stats.serializers import StatItemSerializer
from website_versions.models import WebsiteVersions
from rest_framework import serializers


class WebSiteVersionsSerializer(serializers.ModelSerializer):
    stats = StatItemSerializer(many=True, read_only=True)

    class Meta:
        model = WebsiteVersions
        fields = "__all__"
