from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Store, Location
from .serializers import StoreSerializer

# Create your views here.

class StoreList(generics.ListCreateAPIView):
  """
  ALLOWS TWO METHODS
  GET: List details of all stores
  POST: Create a new store
  """
  queryset = Store.objects.all()
  serializer_class = StoreSerializer

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
  """
    ALLOWS THREE METHODS
    GET: Retrieve detail of a store
    PUT: Update detail of a store
    DELETE: Delete a store
  """
  queryset = Store.objects.all()
  serializer_class = StoreSerializer

  def perform_destroy(self, instance):
    location_id = instance.location.id
    # delete store instance
    instance.delete()
    # delete location instance associated to the store deleted
    Location.objects.get(id=location_id).delete()


class StoreViewSet(ModelViewSet):
  """
  A ViewSet for viewing and editing Stores.
  """
  queryset = Store.objects.all()
  serializer_class = StoreSerializer
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]

  # this can be removed
  def perform_create(self, serializer):
    print('perform_create')
    print(serializer.validated_data)
    serializer.save()

  def perform_destroy(self, instance):
    """
    Deletes Store instance as well as its associated Location instance.
    """
    location_id = instance.location.id
    # delete store instance
    instance.delete()
    # delete location instance associated to the store deleted
    Location.objects.get(id=location_id).delete()