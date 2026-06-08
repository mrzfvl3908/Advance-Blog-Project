from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .paginations import CustomPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category

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

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'author', 'status']
    search_fields = ['title', 'content']
    ordering_fields = ['created_date', 'updated_date']
    pagination_class = CustomPagination
    # lookup_field = 'slug'

    # @action(methods=['get'], detail=False)
    # def get_ok(self,request):
    #     return Response({'detail':'ok'})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
