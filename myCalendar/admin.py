from django.contrib import admin

# Register your models here.
from .models import Entry

### admin
class EntryAdmin(admin.ModelAdmin):
    list_display = ["creator", "date", "title", "snippet"]
    list_filter= ["creator"]

admin.site.register(Entry, EntryAdmin)
