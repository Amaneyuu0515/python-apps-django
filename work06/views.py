from django.shortcuts import render
from .forms import ReiwaForm  # ← これでOK！


def reiwa_to_seireki(request):
    result = None
    if request.method == "POST":
        form = ReiwaForm(request.POST)
        if form.is_valid():
            reiwa_year = form.cleaned_data["year"]
            seireki = 2018 + reiwa_year
            result = f"令和{reiwa_year}年 → 西暦 {seireki}年"
    else:
        form = ReiwaForm()

    return render(request, "work06/reiwa.html",
                  {"form": form, "result": result})
