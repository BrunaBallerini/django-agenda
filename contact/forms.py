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
        help_text='Texto de ajuda'
    )

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Escreva seu nome aqui',
        #         }
        #     ),
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data
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
