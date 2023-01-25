from django.urls import path
from .views import MenuConfigDetail, MenuList, CategoryList

urlpatterns = [
  path('menu-configuration/', MenuConfigDetail.as_view(), name='menu-configuration-detail'),
  path('menus/', MenuList.as_view(), name="menu-list"),
  path('categories/', CategoryList.as_view(), name='category-list'), 
]
