from django.urls import path

from . import views
print("fart2")
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('experience', views.experience, name='experience'),
    path('resume', views.resume, name='resume'),
    path('contacts', views.contacts, name='contacts')
]