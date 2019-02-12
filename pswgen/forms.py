from django import forms


class GeneratePasswordForm(forms.Form):
    psw_length = forms.IntegerField(min_value=6, max_value=32, initial=8)
    # psw = forms.CharField(min_length=6, max_length=32)
