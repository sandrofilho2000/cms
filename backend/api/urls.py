from django.urls import path
import website_versions.views as views

urlpatterns = [
    path("site_data", views.WebSiteVersionDetailView.as_view(), name="site_data"),
    path(
        "site_data/<uuid:pk>/",
        views.WebSiteVersionDetailView.as_view(),
        name="site_data_by_pk",
    ),
]
