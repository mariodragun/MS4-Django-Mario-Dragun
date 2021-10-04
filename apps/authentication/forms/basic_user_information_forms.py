from django import forms


class BasicUserInformationForm(forms.Form):
    first_name = forms.CharField(
        label="First Name",
    )
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="Email")

    def __init__(self, *args, **kwargs):
        super(BasicUserInformationForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs["class"] = "form-control"

    def save(self, user):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")

        # try to store new information if there is anything
        try:
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if email:
                user.email = email

            user.save()
        except Exception:
            pass
