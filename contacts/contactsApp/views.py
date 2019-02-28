from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewContactForm
from .models import Contacts


# Create your views here.
def index(request):
    allcontacts = Contacts.objects.all()
    return render(request, 'contactsApp/index.html', {'contactform': allcontacts})

# add new contact
def contacts(request):
    new_contact = NewContactForm(request.POST or None)
    if new_contact.is_valid():
        new_contact.save()
        return redirect('index')

    context = {
        'contactform': new_contact
    }

    return render(request, 'contactsApp/contacts.html', context)
# edit entry
def editcontact(request, id):
    contact = get_object_or_404(Contacts, pk=id)
    edit_form = NewContactForm(request.POST or None, instance=contact)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')
    return render(request, 'contactsApp/contacts.html', {'contactform': edit_form})
# delete entry
def deletecontact(request, id):
    contact = get_object_or_404(Contacts, pk=id)
    print(request.POST)
    if request.method == 'POST':
        print('********')
        contact.delete()
        return redirect('index')
    return render(request, 'contactsApp/delete.html', {'selectedcontact': contact})

