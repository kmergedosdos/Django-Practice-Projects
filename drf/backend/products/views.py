from rest_framework import generics, mixins, authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
from api.permissions import IsStaffEditorPermission
from api.mixins import StaffEditorPermissionMixin

from api.authentication import TokenAuthentication

# CLASS BASED VIEWS

class ProductListCreateAPIView(generics.ListCreateAPIView, StaffEditorPermissionMixin):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # authentication_classes = [
  #   authentication.SessionAuthentication,
  #   TokenAuthentication
  # ]
  # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    # email = serializer.validated_data.pop('email')
    # print(email)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content') or None
    if content is None:
      content = title
    serializer.save(user=self.request.user,content=content)

  def get_queryset(self, *args, **kwargs):
    qs = super().get_queryset(*args, **kwargs)
    request = self.request
    # print(request.user)
    return qs.filter(user=request.user)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView, StaffEditorPermissionMixin):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
  # lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView, StaffEditorPermissionMixin):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(generics.DestroyAPIView, StaffEditorPermissionMixin):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

  def perform_destroy(self, instance):
    return super().perform_destroy(instance)

product_delete_view = ProductDeleteAPIView.as_view()


# combine different class-based views using mixins and GenericAPIView

class ProductMixinView(
  mixins.CreateModelMixin,
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  generics.GenericAPIView
  ):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  
  # Http GET
  def get(self, request, *args, **kwargs):
    pk = kwargs.get('pk')
    if pk:
      return self.retrieve(request, *args, **kwargs)
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

product_mixin_view = ProductMixinView.as_view()


# FUNCTION BASED VIEWS

@api_view(["GET", "POST"])
def product_alt_view(request, pk = None, *args, **kwargs):
  method = request.method

  if method == "GET":
    if pk is not None:
      # detail view
      obj = get_object_or_404(Product, pk=pk)
      data = ProductSerializer(obj, many=False).data
      return Response(data)
    
    # list view
    queryset = Product.objects.all()
    data = ProductSerializer(queryset, many=True).data
    return Response(data)

  if method == "POST":
    # create an item
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): #make sure that data sent to the endpoint is valid
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content') or None
      if content is None:
        content = title
      serializer.save(content=content)
      return Response(serializer.data)
    return Response({"invalid": "invalid data"}, status=404)


