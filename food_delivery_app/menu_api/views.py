from rest_framework import viewsets, mixins, generics

from .models import MenuConfig, Menu, Category

from .serializers import MenuConfigSerializer, MenuSerializer

from rest_framework.response import Response

# Create your views here.
class MenuConfigViewSet(viewsets.ModelViewSet):
  """
  A ViewSet for viewing and editing Menus.
  """
  serializer_class = MenuConfigSerializer

  def get_queryset(self):
    return MenuConfig.objects.filter(store=self.kwargs['store_pk'])
  
  def list(self, request, *args, **kwargs):
    print(self.kwargs)
    instance = self.get_queryset().get(store=self.kwargs['store_pk'])
    serializer = MenuConfigSerializer(instance)
    print(serializer.data)
    return Response(serializer.data)
  
  def update(self, request, *args, **kwargs):
    print(self.kwargs)
    return Response('updated menu config')
  
class MenuConfigDetail(generics.RetrieveUpdateAPIView):
  """
  View for Menu Configuration Details.
  """
  queryset = MenuConfig.objects.all()
  serializer_class = MenuConfigSerializer
  lookup_field = 'store_id'

class MenuList(generics.ListCreateAPIView):
  serializer_class = MenuSerializer

  def get_queryset(self):
    return Menu.objects.filter(menu_config=MenuConfig.objects.get(store=self.kwargs['store_id']).id)