from links.apps import LinksConfig
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from links.views import LinksIndex, LinkDeleteView, link_redirect

app_name = LinksConfig.name

urlpatterns = [
    path("", LinksIndex.as_view(), name="index"),
    path("delete/<int:pk>", LinkDeleteView.as_view(), name='delete'),
    path("<str:code>", link_redirect, name='redirect'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
