
from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'created_at', 'updated_at')
    search_fields = ('name', 'location')
    list_filter = ('date',)

admin.site.register(Event, EventAdmin)
