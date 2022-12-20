from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('stores/', views.store_list),
    path('stores/<int:pk>/', views.store_detail),
]
