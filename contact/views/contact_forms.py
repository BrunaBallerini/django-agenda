from django.shortcuts import render

from contact.forms import ContactForm


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
