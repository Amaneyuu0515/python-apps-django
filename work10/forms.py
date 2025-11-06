# work10/forms.py
from django import forms
from work09.models import Todo  # ← ここを変更！


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "due_date", "is_completed"]
