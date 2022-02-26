from django.urls import include, path
from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('schema.json', SpectacularJSONAPIView.as_view(), name='schema.json'),
    path('', SpectacularSwaggerView.as_view(url_name='schema.json'), name='swagger'),
    path('news/', include('src.news.urls')),
]
