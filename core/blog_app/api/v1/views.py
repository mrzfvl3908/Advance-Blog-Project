from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404

@api_view()
def postList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view()
def postDetail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    serializer = PostSerializer(post)
    return Response(serializer.data)