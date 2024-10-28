# -*- coding: utf-8 -*-
from django.urls import path

from apps.todos.views import TodoDetailView, TodoListCreateView

urlpatterns = [
    path("todos/", TodoListCreateView.as_view(), name="todo-list-create"),
    path("todos/<int:pk>/", TodoDetailView.as_view(), name="todo-detail"),
]
