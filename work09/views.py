from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from datetime import date


def todo_list(request):
    todos = Todo.objects.all().order_by("due_date")
    form = TodoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("work09:todo_list")

    context = {
        "form": form,
        "todos": todos,
        "today": date.today(),  # ← これを追加
    }
    return render(request, "work09/todo_list.html", context)


def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("work09:todo_list")
    else:
        form = TodoForm(instance=todo)
    return render(request, "work09/todo_form.html", {"form": form})


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("work09:todo_list")


# 追加：これが無くて怒られてます！
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("work09:todo_list")
    else:
        form = TodoForm()
    return render(request, "work09/todo_form.html", {"form": form})
