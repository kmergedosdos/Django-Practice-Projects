from django.urls import path
from .views import MenuConfigDetail, MenuList, MenuDetail, CategoryList, ItemList

urlpatterns = [
  path('menu-configuration/', MenuConfigDetail.as_view(), name='menu-configuration-detail'),
  path('menus/', MenuList.as_view(), name="menu-list"),
  path('menus/<int:pk>/', MenuDetail.as_view(), name="menu-detail"),
  path('categories/', CategoryList.as_view(), name='category-list'),
  path('items/', ItemList.as_view(), name='item-list'),
]
