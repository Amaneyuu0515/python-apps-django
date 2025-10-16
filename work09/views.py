from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todos = Todo.objects.all().order_by("due_date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("work09:todo_list")  # ✅ ← OK
    else:
        form = TodoForm()
    return render(request,
                  "work09/todo_list.html", {"form": form, "todos": todos})


def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("work09:todo_list")  # ✅ ← ここが原因！修正必須！
    else:
        form = TodoForm(instance=todo)
    return render(request, "work09/todo_form.html", {"form": form})


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("work09:todo_list")  # ✅ ← ここも念のため確認


def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("work09:todo_list")  # ✅ ← ここもOK
    else:
        form = TodoForm()
    return render(request, "work09/todo_form.html", {"form": form})
