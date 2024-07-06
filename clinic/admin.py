from django.contrib import admin
from . import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'message', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'message')