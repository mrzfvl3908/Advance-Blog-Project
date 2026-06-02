from rest_framework import serializers
from blog_app.models import Post


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=300)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author','title','content','published_date','status']