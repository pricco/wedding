from django.contrib import admin
from music.models import Song


class SongAdmin(admin.ModelAdmin):

    list_display = ('artist', 'title', 'active',)
    list_filter = ('artist', 'active',)
    search_fields = ('artist', 'title',)

    list_per_page = 1000
    list_max_show_all = 1000

admin.site.register(Song, SongAdmin)