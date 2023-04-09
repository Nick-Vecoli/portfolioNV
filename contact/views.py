from django.shortcuts import render, redirect
from .models import Contact
print("contact submit")


# Create your views here.
def contact(request):
    print(request.method)
    if request.method == "POST":
        print('hello')
        name = request.POST.get('first-name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name= name, surname=surname, email=email, message=message)
        contact.save()
        return redirect('/')