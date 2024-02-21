from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Escreva seu nome aqui',
            }
        ),
        label='Primeiro Nome',
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Escreva sua descrição aqui',
            }
        ),
        label='Descrição',
        help_text='Escreva sua descrição.'
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
                    'placeholder': 'Escreva seu último nome aqui',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Escreva seu número de celular aqui.',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Escreva seu e-mail aqui',
                }
            ),
        }

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg = 'Primeiro nome não pode ser igual ao último nome.'
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
                    'Não digite ABC maiúsculo',
                    code='invalid',
                )
            )
        return first_name
