from django.contrib import admin

# Register your models here.
from .models import Summoner

class SummonerAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,                  {'fields': ['summoner_id']}),
        (None,                  {'fields': ['name']}),
        (None,                  {'fields': ['std_name']}),
        (None,                  {'fields': ['profile_icon_id']}),
        (None,                  {'fields': ['summoner_level']}),
        (None,                  {'fields': ['region']}),
        (None,                  {'fields': ['revision_date']}),
#        ('Date information',    {'fields': ['last_update'], 'classes': ['collapse']}),
    ]

    list_display = ('summoner_id', 'name', 'last_update')
    list_filter = ['last_update']
    search_fields = ['name', 'last_update']


admin.site.register(Summoner, SummonerAdmin)
