from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')

    context = {
        'site_title': 'Register user',
        'form': form,
    }

    return render(
        request,
        'contact/register.html',
        context,
    )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login successful')
            return redirect('contact:index')
        messages.error(request, 'Invalid login')

    context = {
        'site_title': 'Login',
        'form': form,
    }

    return render(
        request,
        'contact/login.html',
        context,
    )


def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')
