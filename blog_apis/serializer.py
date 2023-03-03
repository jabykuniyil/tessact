from rest_framework import serializers
from .models import Blog
from user.models import UserProfile


class BlogSerializer(serializers.ModelSerializer):
    blog_author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Blog
        fields = [
            'title',
            'blog_content',
            'media_url',
            'created_by',
            'created_at',
            'blog_author'
        ]

    def get_blog_author(self, obj):
        author = UserProfile.objects.get(id=obj.created_by_id)
        author_name = f"{author.first_name} {author.last_name}"
        return author_name
