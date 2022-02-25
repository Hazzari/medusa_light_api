from django.urls import include, path
from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('schema.json', SpectacularJSONAPIView.as_view(), name='schema.json'),
    path('apidocs/', SpectacularSwaggerView.as_view(url_name='schema.json'), name='swagger'),
    path('apiredocs/', SpectacularRedocView.as_view(url_name='schema.json '), name='redocs'),
    path('news/', include('src.news.urls')),
]
