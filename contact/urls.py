from django.urls import path

from . import views

print("fart")
urlpatterns = [
    path('contact', views.contact, name='contact')
]