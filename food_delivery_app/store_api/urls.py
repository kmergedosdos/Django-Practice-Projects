from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# urlpatterns = [
#     path('stores/', views.StoreList.as_view()),
#     path('stores/<int:pk>/', views.StoreDetail.as_view()),
# ]

router = DefaultRouter()
router.register(r'stores', views.StoreViewSet, basename='store')
urlpatterns = router.urls