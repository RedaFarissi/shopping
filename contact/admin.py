from django.contrib import admin
from .models import ContactUser


class ContactUserAdmin(admin.ModelAdmin):
    list_display = ['subject' ,'email' ,'message' ,'contact_date' ,'vu' ]
    list_editable = ['vu']
    list_filter = ['contact_date']


admin.site.register(ContactUser, ContactUserAdmin)