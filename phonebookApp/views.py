from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader

from phonebookApp.forms import ContactForm
from phonebookApp.models import Contact


class x:
    def __init__(self):
        pass


def show_all_contacts(request):
    return HttpResponse("You're looking at all contacts.")


def index(request):
    z = x()
    z.question_text = "What's new?"
    latest_question_list = [z]
    template = loader.get_template("phonebook/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')  # Redirect to a list view or success page
    else:
        form = ContactForm()
    return render(request, 'phonebook/add_contact.html', {'form': form})


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'phonebook/contact_list.html', {'contacts': contacts})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'phonebook/contact_detail.html', {'contact': contact})
