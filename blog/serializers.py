from blog.models import Post
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date', 'published_date', 'image')