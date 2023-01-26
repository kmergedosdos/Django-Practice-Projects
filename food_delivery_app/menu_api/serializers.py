from rest_framework import serializers
from .models import MenuConfig, Menu, Category, Item


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
  menu_config = serializers.PrimaryKeyRelatedField(read_only=True)
  
  class Meta:
    model = Menu
    fields = [
      'title',
      'subtitle',
      'menu_config'
    ]
  
  def create(self, validated_data):
    menu_instance = Menu.objects.create(**validated_data)
    return menu_instance


class CategorySerializer(serializers.ModelSerializer):
  menu_config = serializers.PrimaryKeyRelatedField(read_only=True)

  class Meta:
    model = Category
    fields = [
      'title',
      'subtitle',
      'menu_config'
    ]
  
  def create(self, validated_data):
    category_instance = Category.objects.create(**validated_data)
    return category_instance


class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = '__all__'