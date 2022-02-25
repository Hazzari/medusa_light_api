from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import NewsPost
from .serializers import NewsPostListSerializer


class NewsPostViewSet(ModelViewSet):
    """Новостные посты."""

    queryset = NewsPost.objects.all().order_by('-date')
    serializer_class = NewsPostListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
