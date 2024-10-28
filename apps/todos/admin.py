# -*- coding: utf-8 -*-
from django.contrib import admin

from apps.todos.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
