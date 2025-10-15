from django.urls import path
from . import views

app_name = "work07"

urlpatterns = [
    path('', views.top, name='top'),           # トップページ
    path('omikuji/', views.omikuji, name='omikuji'),  # おみくじページ
]
