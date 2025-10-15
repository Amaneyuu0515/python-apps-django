from django.urls import path
from . import views

app_name = "work08"

urlpatterns = [
    path("", views.memo_list, name="list"),
    path("new/", views.memo_new, name="new"),
    path("edit/<int:memo_id>/", views.memo_edit, name="edit"),  # ←これ大事！
]
