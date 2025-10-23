from django.urls import path
from . import views

app_name = "work10"

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("delete/<int:pk>/", views.todo_delete, name="todo_delete"),
    path("signup/", views.signup, name="signup"),  # ←★これを必ず追加
    path("auth_home/", views.auth_home, name="auth_home"),
]
