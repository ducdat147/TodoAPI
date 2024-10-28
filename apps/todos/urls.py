# -*- coding: utf-8 -*-
from django.urls import path

from apps.todos.views import LoginView, TodoDetailView, TodoListCreateView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("todos/", TodoListCreateView.as_view(), name="todo-list-create"),
    path("todos/<uuid:pk>/", TodoDetailView.as_view(), name="todo-detail"),
]
