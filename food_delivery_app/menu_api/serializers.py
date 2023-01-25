from rest_framework import serializers
from .models import MenuConfig, Menu, Category

class MenuConfigSerializer(serializers.ModelSerializer):
  menus = serializers.HyperlinkedIdentityField(
    view_name='menu-list',
    lookup_field='store_id'
  )
  categories = serializers.HyperlinkedIdentityField(
    view_name='category-list',
    lookup_field='store_id'
  )

  class Meta:
    model = MenuConfig
    fields = [
      'id',
      'store',
      'menus',
      'categories'
    ]

class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'