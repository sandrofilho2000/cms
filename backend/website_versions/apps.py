from django.apps import AppConfig


class WebsiteVersionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website_versions'
    verbose_name="Variante do site"
    verbose_name_plural="Variantes do site"
