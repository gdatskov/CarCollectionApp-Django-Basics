from django import forms

from car_collection.car_collection_app.models import Profile, Car

"""
•	A profile creation form consisting of:
o	An "Username:" field
o	An "Email:" field
o	An "Age:" field
o	A "Password:" field. In the form, the characters must be hidden.
•	A button "Create Profile"
o	When you click on it, if the profile is successfully created, you should be redirected to the catalogue page.
o	Otherwise, the form should show the appropriate validation errors in the form.
"""


class BaseProfileMetaForm:
    model = Profile
    widgets = {
        'password': forms.PasswordInput(),
    }


class CreateProfileForm(forms.ModelForm):
    class Meta(BaseProfileMetaForm):
        fields = ['username', 'email', 'age', 'password']


class EditProfileForm(forms.ModelForm):
    class Meta(BaseProfileMetaForm):
        exclude = ['password']


class DeleteProfileForm(EditProfileForm):
    class Meta(BaseProfileMetaForm):
        fields = ()




class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'car_image_url': 'Image URL'
        }


class CreateCarForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
