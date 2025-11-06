# work10/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# from .models import Todo ← ここを削除！
from work09.models import Todo  # ← ★ work09 からTodoをインポート！


def todo_list(request):
    todos = Todo.objects.all().order_by("due_date")
    return render(request, "work10/todo_list.html", {"todos": todos})


def auth_home(request):
    return render(request, "work10/auth_home.html")


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("work10:todo_list")
    return render(request, "work10/todo_delete.html", {"todo": todo})


def signup(request):
    """ユーザー登録ページ"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("work10:todo_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
