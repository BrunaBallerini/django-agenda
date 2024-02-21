from django.shortcuts import redirect, render

from contact.forms import ContactForm


def create(request):
    if request.method == 'POST':

        form = ContactForm(data=request.POST)

        context = {
            'site_title': 'Cria contatos',
            'form': form,
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.show = True
            contact.save()
            return redirect('contact:index')

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
