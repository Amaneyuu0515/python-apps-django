from django.contrib import admin
from django.urls import path

from . import views  # views モジュールをインポート

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index, name="index"),  # views.index が存在することを確認
]