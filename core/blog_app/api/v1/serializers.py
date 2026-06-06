from django.template.context_processors import request
from rest_framework import serializers
from blog_app.models import Post, Category


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=300)

class PostSerializer(serializers.ModelSerializer):
    # content = serializers.ReadOnlyField()
    snippet = serializers.ReadOnlyField(source='get_snippet')  # => ارتباط گیری با فانکشن نوشته شده در مدل
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'published_date', 'status', 'snippet', 'absolute_url']

        # read_only_fields = ['content']

    def get_abs_url(self, obj):
        request = self.context.get('request')

        if request:
            return request.build_absolute_uri(
                obj.get_absolute_url()
            )

        return obj.get_absolute_url()


# class PostSerializer(serializers.HyperlinkedModelSerializer): راه حرفه ای تر برای ننوشتن متد پست برای نمایش url
#     class Meta:
#         model = Post
#         fields = (
#             'url',
#             'id',
#             'title',
#             'content',
#         )
#
#     url = serializers.HyperlinkedIdentityField(
#         view_name='post-detail',
#         lookup_field='slug'
#     )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
