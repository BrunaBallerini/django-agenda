from typing import Any

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid',
        #     ),
        # )

        # self.add_error(
        #     None,
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid',
        #     ),
        # )

        return super().clean()


def create(request):
    if request.method == 'POST':

        context = {
            'site_title': 'Cria contatos',
            'form': ContactForm(data=request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'site_title': 'Cria contatos',
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context,
    )
