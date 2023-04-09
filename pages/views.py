from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def experience(request):
    return render(request, 'pages/experience.html')

def contacts(request):
    return render(request, 'pages/contact.html')

def resume(request):
    return render(request, 'pages/resume.html')
