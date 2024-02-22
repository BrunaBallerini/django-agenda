from django.contrib import messages
from django.shortcuts import render

from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')

    context = {
        'site_title': 'Cria usuário',
        'form': form,
    }

    return render(
        request,
        'contact/register.html',
        context,
    )
