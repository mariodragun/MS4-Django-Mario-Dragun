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
