from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, BasePermission, SAFE_METHODS


class PostUserWritePermission(BasePermission):
  message = 'Editing posts is restricted to the author only.'

  def has_object_permission(self, request, view, obj):
    if request.method in SAFE_METHODS:
      return True

    return request.user == obj.author

class PostList(generics.ListCreateAPIView):
  queryset = Post.postobjects.all()
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  
class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [PostUserWritePermission]