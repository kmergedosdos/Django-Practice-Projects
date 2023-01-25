from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoreViewSet
from menu_api.views import MenuConfigDetail, MenuList, CategoryList

router = DefaultRouter()
router.register(r'stores', StoreViewSet, basename='store')

urlpatterns = [
  path('', include(router.urls)),
  path('stores/<int:store_id>/', include('menu_api.urls')),
]