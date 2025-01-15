from django.contrib import admin
from contact.models import Contact


class ContactModelAdmin(admin.ModelAdmin):

    class Meta:
        list_display = '__all__'
        search_field = ('subject')

admin.site.register(Contact, ContactModelAdmin)
