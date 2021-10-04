from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(),
    )

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs["class"] = "form-control"

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # check if the password is set correctly and that both values are the same
        if password != confirm_password:
            msg = "Password and Confirm Password should be the same value."
            self.add_error("password", msg)
            self.add_error("confirm_password", msg)

    def save(self, user):
        # get cleaned data
        cleaned_data = self.cleaned_data

        # set new user password
        user.password = make_password(cleaned_data.get("password"))
        user.save()
