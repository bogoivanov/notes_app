from django import forms
from django.core.exceptions import ValidationError

from notes_app.my_web.models import Profile, Note


def validate_only_chars(value):
    if not value.isalpha():
        raise ValidationError('Can contain only letters')


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Link to Profile Image',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'age': forms.TextInput(attrs={'placeholder': 'Enter AGE'}),
            'image_url': forms.TextInput(
                attrs={'placeholder': 'Enter URL here'}),
        }


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            'title',
            'content',
            'image_url',
        )
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter Content'}),
            'image_url': forms.TextInput(
                attrs={'placeholder': 'Enter URL here'}),
        }

class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            'title',
            'content',
            'image_url',
        )


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = (
            'title',
            'content',
            'image_url',
        )
