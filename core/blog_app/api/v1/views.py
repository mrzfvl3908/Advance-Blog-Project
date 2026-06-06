from django.core.serializers import serialize
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

"""
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


# class PostDetail(APIView):
#     ''' GEETING DETAIL OF THE POST AND EDIT PLUS REMOVING IT '''
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#
#     def get(self, request, slug):
#         ''' retriveing the post data '''
#         post = get_object_or_404(Post, slug=slug)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
#
#     def put(self, request, slug):
#         ''' editing the post data '''
#         post = get_object_or_404(Post, slug=slug)
#         serializer = self.serializer_class(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, slug):
#         ''' deleting post '''
#         post = get_object_or_404(Post, slug=slug)
#         post.delete()
#         return Response({"detail": "post delete successfully"}, status=status.HTTP_204_NO_CONTENT)



# class PostList(ListAPIView, ListCreateAPIView):
#     ''' getting post for list and create post '''
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
# 
# 
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     ''' GEETING DETAIL OF THE POST AND EDIT PLUS REMOVING IT '''
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
"""

# Example for viewset in cbv

class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        post_object = get_object_or_404(Post, id=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, slug):
        pass

    def partial_update(self, request, slug):
        pass

    def destroy(self, request, slug):
        pass


