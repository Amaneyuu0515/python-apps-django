from django.shortcuts import render, get_object_or_404, redirect
from .models import Memo


def memo_list(request):
    memos = Memo.objects.all().order_by("-updated_at")
    return render(request, "work08/list.html", {"memos": memos})


def memo_new(request):
    memo = Memo.objects.create()
    return redirect("work08:edit", memo_id=memo.id)


def memo_edit(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)

    if request.method == "POST":
        memo.title = request.POST.get("title", memo.title)
        memo.content = request.POST.get("content", memo.content)
        memo.save()
        return redirect("work08:list")

    return render(request, "work08/edit.html", {"memo": memo})
