from django.shortcuts import render, get_object_or_404
from banners.models import Banner
from banners.serializers import BannerSerializer
from color_palette.serializers import ColorPaletteSerializer
from color_palette.models import ColorPalette
from faq.models import Faq, FaqItem
from faq.serializers import FaqItemSerializer, FaqSerializer
from features.models import Feature
from features.serializers import FeatureSerializer
from hero.models import Hero
from hero.serializers import HeroSerializer
from icons.models import Icon
from icons.serializers import IconSerializer
from website_versions.models import WebsiteVersions
from website_versions.serializers import WebSiteVersionsSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


class WebSiteVersionDetailView(generics.GenericAPIView):
    serializer_class = WebSiteVersionsSerializer
    queryset = WebsiteVersions.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")

        if pk:
            instance = get_object_or_404(WebsiteVersions, pk=pk)
        else:
            instance = self.get_queryset().filter(active=True).first()
            if not instance:
                raise NotFound("No active website version found.")

        website_version = self.get_serializer(instance).data

        color_palette_instance = get_object_or_404(
            ColorPalette, pk=website_version["color_palette"]
        )
        color_palette = ColorPaletteSerializer(color_palette_instance).data

        hero_instance = get_object_or_404(Hero, pk=website_version["hero"])
        hero = HeroSerializer(hero_instance).data

        stats = []

        for stat in website_version["stats"]:

            icon_instance = get_object_or_404(Icon, pk=stat["icon"])
            icon = IconSerializer(icon_instance).data

            stat["icon"] = icon["code"]

            stats.append(stat)

        features = []

        for feature in website_version["features"]:

            feature_instance = get_object_or_404(Feature, pk=feature)
            feature = FeatureSerializer(feature_instance).data
            features.append(feature)

        banner_instance = get_object_or_404(Banner, pk=website_version["banner"])
        banner = BannerSerializer(banner_instance).data

        faq_instance = get_object_or_404(Faq, pk=website_version["faq"])
        faq = FaqSerializer(faq_instance).data

        questions = []
        for question in faq["questions"]:
            faq_item_instance = get_object_or_404(FaqItem, pk=question)
            faq_item = FaqItemSerializer(faq_item_instance).data
            questions.append(faq_item)

        faq["questions"] = questions

        response_data = {
            "color_palette": color_palette,
            "hero": hero,
            "stats": stats,
            "features": features,
            "banner": banner,
            "faq": faq,
        }

        return Response(response_data)


def home(request):
    active_version = WebsiteVersions.objects.filter(active=True).first()
    return render(request, "website_versions/base.html", {"version": active_version})
