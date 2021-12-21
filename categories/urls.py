from django.urls import path

# list of accessible paths
from categories import views

urlpatterns = [
    path('', views.get_routes),
    path('categories/', views.get_categories),
    path('categories/create/', views.create_category),
    path('categories/<str:pk>/update/', views.update_category),
    path('categories/<str:pk>/delete/', views.delete_category),
    path('categories/<str:pk>/', views.get_category),
]
