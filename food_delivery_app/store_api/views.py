from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Store
from .serializers import StoreSerializer

# Create your views here.
@api_view(["GET"])
def apiOverview(request):
  return Response("hello world!!!")

@api_view(['GET', 'POST'])
def store_list(request):
  """
  ALLOWS TWO METHODS
  GET: List details of all stores
  POST: Create a new store
  """
  if request.method == "GET":
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)

  elif request.method == "POST":
    serializer = StoreSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def store_detail(request, pk):
  """
  ALLOWS THREE METHODS
  GET: Retrieve detail of a store
  PUT: Update detail of a store
  DELETE: Delete a store
  """ 
  try:
    store = Store.objects.get(pk=pk)
  except Store.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = StoreSerializer(store)
    return Response(serializer.data)

  elif request.method == "PUT":
    serializer = StoreSerializer(store, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == "DELETE":
    store.delete()
    return Response(status=status.HTTP_204_NO_CONTE)
