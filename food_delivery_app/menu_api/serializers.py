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
  items = serializers.HyperlinkedIdentityField(
    view_name='item-list',
    lookup_field='store_id'
  )

  class Meta:
    model = MenuConfig
    fields = [
      'id',
      'store',
      'menus',
      'categories',
      'items'
    ]


class MenuSerializer(serializers.ModelSerializer):
  menu_config = serializers.PrimaryKeyRelatedField(read_only=True)
  categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  
  class Meta:
    model = Menu
    depth = 1
    fields = [
      'id',
      'title',
      'subtitle',
      'menu_config',
      'categories',
      'items',
    ]
  
  def create(self, validated_data):
    menu_instance = Menu.objects.create(**validated_data)
    return menu_instance


class CategorySerializer(serializers.ModelSerializer):
  menu_config = serializers.PrimaryKeyRelatedField(read_only=True)

  class Meta:
    model = Category
    depth = 1
    fields = [
      'id',
      'title',
      'subtitle',
      'menu_config',
      'items'
    ]
  
  def create(self, validated_data):
    category_instance = Category.objects.create(**validated_data)
    return category_instance


class ItemSerializer(serializers.ModelSerializer):
  menu_config = serializers.PrimaryKeyRelatedField(read_only=True)
  is_available = serializers.BooleanField(default=True)
  
  class Meta:
    model = Item
    fields = [
      'id',
      'title',
      'subtitle',
      'image_url',
      'price',
      'is_available',
      'menu_config',
      'menu',
      'category'
    ]

  def create(self, validated_data):
    menu = validated_data.get('menu', None)
    category = validated_data.get('category', None)

    # add category to menu categories
    menu.categories.add(category)

    return Item.objects.create(**validated_data)
