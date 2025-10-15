# filepath: /Users/kanekokeigo/Desktop/python-apps-django/python-apps-django-1/
# work05/views.py
from django.shortcuts import render


def index(request):
    return render(request, "work05/index.html")
