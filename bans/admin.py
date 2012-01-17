from bans.models import Ban
from django.contrib import admin
from datetime import datetime

class BanAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User Info',  {'fields': ['user', 'banned_by',]}),
        ('Dates',      {'fields': ['start_dtm', 'end_dtm',]}),
        ('Other Info', {'fields': ['permaban', 'ip_address',
                                   'reason', 'notes',]})]
    list_display = ('user', 'start_dtm', 'end_dtm')
    list_filter = ['end_dtm']
    search_fields = ('user', 'banned_by')

    def currently_banned(self):
        return self.end_dtm.date >= datetime.date.today()
    currently_banned.short_description = 'Currently banned?'

admin.site.register(Ban, BanAdmin)
