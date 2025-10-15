from django.urls import path
from . import views

urlpatterns = [
    path("reiwa/", views.reiwa_to_seireki, name="reiwa"),
]
