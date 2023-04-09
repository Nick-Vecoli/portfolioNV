from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'message')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)    
# Register your models here.
