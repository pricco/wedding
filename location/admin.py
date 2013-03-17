from django.contrib import admin
from location.models import Location


class LocationAdmin(admin.ModelAdmin):

    list_display = ('title', 'latitude', 'longitude',)
    search_fields = ('title', 'description',)

    list_per_page = 1000
    list_max_show_all = 1000

admin.site.register(Location, LocationAdmin)