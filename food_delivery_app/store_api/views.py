from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

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