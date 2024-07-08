from django.contrib import admin
from resapp.models import Contacts
# Register your models here.
@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['username','email','msg']