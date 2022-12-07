from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
  """
  get -> list -> queryset
  get -> retrieve => Product intance detail view
  post -> create -> New Instance
  put -> update
  patch -> Partial Update
  delete -> destroy
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
  ):
  """
  get -> list -> queryset
  get -> retrieve -> Product intance detail view
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'