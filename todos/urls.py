from django.urls import path
from .views import CategoryListApiView, CategoryDetailApiView, CategorySearchAPIView, TaskListApiView, TaskDetailsApiView, TaskApiSearchView


urlpatterns = [
    path("categories/", CategoryListApiView.as_view(), name="categories"),
    path("categories/<int:pk>/", CategoryDetailApiView.as_view(), name="category-details"),
    path('categories/search/', CategorySearchAPIView.as_view(), name='categories-search'),

    path("tasks/", TaskListApiView.as_view(), name="tasks"),
    path("tasks/<int:pk>/", TaskDetailsApiView.as_view(), name="task-details"),
    path("tasks/search/", TaskApiSearchView.as_view(), name="tasks-search")
]
