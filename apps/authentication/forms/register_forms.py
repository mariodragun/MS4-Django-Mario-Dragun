from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserRegisterForm(forms.Form):
    """User Register form which will be used in a Register FormView."""

    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")

    email = forms.EmailField(label="email")
    username = forms.CharField(label="Username")

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(),
    )
    confirm_password = forms.CharField(
        label="Change Password",
        strip=False,
        widget=forms.PasswordInput(),
    )

    def clean(self):
        """Overwriting clean method which and expanding functionlity to check:
        - if username is taken
        - if provided password and confirm_password fields have same value
        """

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # check if username is already taken
        user = User.objects.filter(username=cleaned_data.get("username"))
        if user:
            self.add_error("username", "That username is already taken.")

        # check if the password is set correctly and that both values are the same
        if password != confirm_password:
            msg = "Password and Confirm Password should be the same value."
            self.add_error("password", msg)
            self.add_error("confirm_password", msg)

    def save(self):
        """Save method which will store form information in the database, and
        with that it will create a new User object.
        """

        cleaned_data = self.cleaned_data

        # create a new user object with form information
        # also using make_password to hash password information correctly
        user = User(
            username=cleaned_data.get("username"),
            email=cleaned_data.get("email"),
            password=make_password(cleaned_data.get("password")),
            first_name=cleaned_data.get("first_name"),
            last_name=cleaned_data.get("last_name"),
        )
        # set user as active
        user.is_active = True

        # store user information
        user.save()
