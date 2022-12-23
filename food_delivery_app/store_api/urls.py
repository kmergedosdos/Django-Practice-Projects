from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ApiOverview.as_view()),
    path('stores/', views.StoreList.as_view()),
    path('stores/<int:pk>/', views.StoreDetail.as_view()),
]
