from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'title',
            'blog_content',
            'media_url',
            'created_by',
            'created_at'
        ]
