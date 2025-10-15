from django.shortcuts import render
import random


# トップページ
def top(request):
    return render(request, "work07/top.html")


# おみくじページ
def omikuji(request):
    results = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
    # 初期表示でも結果を表示
    result = random.choice(results)
    return render(request, "work07/omikuji.html", {"result": result})
