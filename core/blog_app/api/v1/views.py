from django.core.serializers import serialize
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404


# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
# def postList(request):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def postDetail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response({"detail": "post delete successfully"}, status=status.HTTP_204_NO_CONTENT)


class PostList(APIView):
    ''' getting post for list and create post '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        '''get post for list'''
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        ''' create a new post '''
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PostDetail(APIView):
    ''' GEETING DETAIL OF THE POST AND EDIT PLUS REMOVING IT '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, slug):
        ''' retriveing the post data '''
        post = get_object_or_404(Post, slug=slug)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, slug):
        ''' editing the post data '''
        post = get_object_or_404(Post, slug=slug)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, slug):
        ''' deleting post '''
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return Response({"detail": "post delete successfully"}, status=status.HTTP_204_NO_CONTENT)
