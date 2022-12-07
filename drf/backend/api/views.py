# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
import json

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
  """
  DRF API View
  """

  # makes sure that data sent to the endpoint is valid
  serializer = ProductSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    # serializer.save() # saves the data as Product instance
    print(serializer.data)
    return Response(serializer.data)

  # instance = Product.objects.all().order_by("?").first()
  # data = {}
  # if instance:
  #   # data = model_to_dict(instance)
  #   data = ProductSerializer(instance).data
  # return Response(data)