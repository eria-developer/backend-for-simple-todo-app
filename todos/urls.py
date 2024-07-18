from django.urls import path
from .views import CategoryListApiView, CategoryDetailApiView


urlpatterns = [
    path("categories/", CategoryListApiView.as_view(), name="categories"),
    path("categories/<int:pk>", CategoryDetailApiView.as_view(), name="category-details")
]
