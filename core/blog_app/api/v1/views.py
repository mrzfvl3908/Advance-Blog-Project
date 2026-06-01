from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post

@api_view()
def postList(request):
    return Response('OK')

@api_view()
def postDetail(request,slug):
    return Response(slug)