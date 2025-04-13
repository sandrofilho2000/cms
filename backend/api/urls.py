from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from website_versions import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("api/site_data", views.WebSiteVersionDetailView.as_view(), name="site_data"),
    path(
        "api/site_data/<int:pk>/",
        views.WebSiteVersionDetailView.as_view(),
        name="site_data_by_pk",
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
