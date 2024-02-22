from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Write your first name here',
            }
        ),
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Write your description here',
            }
        ),
        label='Description',
        help_text='Write something about youself.'
    )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
    )

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',
        )
        widgets = {
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Write your last name here',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Write your phone number here',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Write your email here',
                }
            ),
        }

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg = 'The first name cannot be the same as the las name.'
            self.add_error(
                'last_name',
                ValidationError(
                    msg,
                    code='invalid'
                )
            )

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Do not type ABC',
                    code='invalid',
                )
            )
        return first_name


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
    )

    last_name = forms.CharField(
        required=True,
    )

    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'Este campo é obrigatório'
        }
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'E-mail já existente',
                    code='invalid',
                )
            )
        return email
