from rest_framework import serializers

from .models import NewsPost


class NewsPostListSerializer(serializers.ModelSerializer):
    """News Post"""

    class Meta:
        model = NewsPost
        fields = "__all__"
