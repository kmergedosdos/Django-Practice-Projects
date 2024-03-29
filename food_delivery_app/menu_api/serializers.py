from rest_framework import serializers
from rest_framework.reverse import reverse
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

# Menu Serializers

class MenuHyperlink(serializers.HyperlinkedIdentityField):

  def get_url(self, obj, view_name, request, format):
    url_kwargs = {
      'store_id': obj.menu_config.store_id,
      'pk': obj.pk
    }
    return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

class MenuSerializer(serializers.ModelSerializer):
  menu_config = serializers.PrimaryKeyRelatedField(read_only=True)
  categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  url = MenuHyperlink(view_name='menu-detail')
  
  class Meta:
    model = Menu
    depth = 1
    fields = [
      'id',
      'title',
      'subtitle',
      'url',
      'menu_config',
      'categories',
      'items',
    ]
  
  def create(self, validated_data):
    menu_instance = Menu.objects.create(**validated_data)
    return menu_instance

# Category Serializers

class CategoryHyperlink(serializers.HyperlinkedIdentityField):
  def get_url(self, obj, view_name, request, format):
    url_kwargs = {
      'store_id': obj.menu_config.store_id,
      'pk': obj.pk
    }
    return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

class CategorySerializer(serializers.ModelSerializer):
  menu_config = serializers.PrimaryKeyRelatedField(read_only=True)
  url = CategoryHyperlink(view_name='category-detail')

  class Meta:
    model = Category
    depth = 1
    fields = [
      'id',
      'title',
      'subtitle',
      'url',
      'menu_config',
      'items'
    ]
  
  def create(self, validated_data):
    category_instance = Category.objects.create(**validated_data)
    return category_instance

# Item Serializers

class ItemHyperlink(serializers.HyperlinkedIdentityField):
  def get_url(self, obj, view_name, request, format):
    url_kwargs = {
      'store_id': obj.menu_config.store_id,
      'pk': obj.pk
    }
    return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

class ItemSerializer(serializers.ModelSerializer):
  menu_config = serializers.PrimaryKeyRelatedField(read_only=True)
  is_available = serializers.BooleanField(default=True)
  url = ItemHyperlink(view_name='item-detail')
  
  class Meta:
    model = Item
    fields = [
      'id',
      'title',
      'subtitle',
      'image_url',
      'price',
      'is_available',
      'url',
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
