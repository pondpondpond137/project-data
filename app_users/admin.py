from django.contrib import admin
from app_users.models import ListContact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'message']

# Register your models here.
admin.site.register(ListContact, ContactAdmin)