from django import forms
from cloudinary.forms import CloudinaryFileField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import BookPost


class BookForm(forms.ModelForm):
    """
    Form to Add and Edit property for booking that uses crispy forms
    """

    class Meta:
        model = BookPost
        fields = [
            "title",
            "description",
            "accommodation_type",
            "city",
            "price_per_night",
            "booking_image",
            "owner_email",
            "owner_phone",
        ]

        widgets = {
            "booking_image": forms.FileInput(
                attrs={"class": "custom-file-input"}
            ),
        }

    def __init__(self, *args, **kwargs):

        super(BookForm, self).__init__(*args, **kwargs)

        # Hides part of image field in crispy if not required during the update
        if self.instance and self.instance.pk:
            self.fields["booking_image"].required = False

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("title"),
            Field(
                "description", maxlength="600", placeholder="Add some details"
            ),
            Field("accommodation_type"),
            Field("city"),
            Field("price_per_night", label="Price per night, &euro;"),
            Field("booking_image"),
            Field("owner_email"),
            Field("owner_phone", placeholder="Defaults to Irish numbers"),
            Submit(
                "submit", "Add my property!", css_class="btn btn-success my-4"
            ),
        )
