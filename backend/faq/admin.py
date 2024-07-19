from django.contrib import admin
from faq.models import Faq, FaqItem


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "subtitle"]


@admin.register(FaqItem)
class FaqItemAdmin(admin.ModelAdmin):
    list_display = ["question", "answer"]
