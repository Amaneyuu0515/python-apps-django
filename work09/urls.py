from django.urls import path
from . import views

app_name = "work09"  # ← これがないと名前空間エラーが出る！

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("<int:pk>/edit/", views.todo_update, name="todo_update"),
    path("<int:pk>/delete/", views.todo_delete, name="todo_delete"),
    path("create/", views.todo_create, name="todo_create"),
]
