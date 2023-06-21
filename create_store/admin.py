from django.contrib import admin
from .models import Store


class StoreAdmin(admin.ModelAdmin):
    list_display = ['user', 'slug', 'created', 'image']
    prepopulated_fields = {'slug': ('user',)}
    list_filter = ['created']

admin.site.register(Store, StoreAdmin)