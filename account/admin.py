from django.contrib import admin
from account.models import User
from django.contrib.auth.models import Group


class UserAdmin(admin.ModelAdmin):

    list_display = ('email',)

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)