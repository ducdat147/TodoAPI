# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.todos.models import Todo

# Create your tests here.


class TodoAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.todo = Todo.objects.create(
            title="Test Todo", description="Description", completed=False
        )

    def test_list_todos(self):
        response = self.client.get(reverse("todo-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo(self):
        data = {
            "title": "New Todo",
            "description": "New description",
            "completed": False,
        }
        response = self.client.post(reverse("todo-list-create"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_todo(self):
        response = self.client.get(reverse("todo-detail", kwargs={"pk": self.todo.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo(self):
        data = {
            "title": "Updated Todo",
            "description": "Updated description",
            "completed": True,
        }
        response = self.client.put(
            reverse("todo-detail", kwargs={"pk": self.todo.id}), data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todo(self):
        response = self.client.delete(
            reverse("todo-detail", kwargs={"pk": self.todo.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
