from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, TagListCreateView, TagRetrieveUpdateDestroyView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagRetrieveUpdateDestroyView.as_view(), name='tag-retrieve-update-destroy'),
]
