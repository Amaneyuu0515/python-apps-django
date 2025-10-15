from django import forms


class ReiwaForm(forms.Form):
    year = forms.IntegerField(
        label="令和の年", min_value=1, help_text="例: 令和5年なら 5 と入力してください"
    )
