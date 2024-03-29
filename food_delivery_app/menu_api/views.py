from rest_framework import generics
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import MenuConfig, Menu, Category, Item
from .serializers import MenuConfigSerializer, MenuSerializer, CategorySerializer, ItemSerializer

# Create your views here.

class MenuConfigDetail(generics.RetrieveUpdateAPIView):
  """
  View for Menu Configuration Details.
  """
  queryset = MenuConfig.objects.all()
  serializer_class = MenuConfigSerializer
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]
  lookup_field = 'store_id'

#Menu Views

class MenuList(generics.ListCreateAPIView):
  serializer_class = MenuSerializer
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    return Menu.objects.filter(menu_config=MenuConfig.objects.get(store=self.kwargs['store_id']).id)
  
  def perform_create(self, serializer):
    # pass the current Store's MenuConfig object to the menu_config field
    serializer.save(menu_config=MenuConfig.objects.get(store=self.kwargs['store_id']))

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = MenuSerializer
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]
  lookup_field = 'pk'
  
  def get_queryset(self):
    return Menu.objects.filter(menu_config=MenuConfig.objects.get(store=self.kwargs['store_id']).id)

#Category Views

class CategoryList(generics.ListCreateAPIView):
  serializer_class = CategorySerializer
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    return Category.objects.filter(menu_config=MenuConfig.objects.get(store=self.kwargs['store_id']).id)
  
  def perform_create(self, serializer):
    # pass the current Store's MenuConfig object to the menu_config field
    serializer.save(menu_config=MenuConfig.objects.get(store=self.kwargs['store_id']))

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = CategorySerializer
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]
  lookup_field = 'pk'

  def get_queryset(self):
    return Category.objects.filter(menu_config=MenuConfig.objects.get(store=self.kwargs['store_id']).id)

# Item Views

class ItemList(generics.ListCreateAPIView):
  serializer_class = ItemSerializer
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    return Item.objects.filter(menu_config=MenuConfig.objects.get(store=self.kwargs['store_id']).id)
  
  def perform_create(self, serializer):
    menu = serializer.validated_data.get('menu', None)
    category = serializer.validated_data.get('category', None)

    # validation
    if menu.menu_config.store_id != self.kwargs['store_id']:
      raise serializers.ValidationError({
        "menu": "This menu must exist in the store."
      })
    if category.menu_config.store_id != self.kwargs['store_id']:
      raise serializers.ValidationError({
        "category": "This category must exist in the store."
      })
    
    # save validated data
    serializer.save(menu_config=MenuConfig.objects.get(store=self.kwargs['store_id']))

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ItemSerializer
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]
  lookup_field = 'pk'

  def get_queryset(self):
    return Item.objects.filter(menu_config=MenuConfig.objects.get(store=self.kwargs['store_id']).id)
