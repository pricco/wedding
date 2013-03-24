from django.contrib import admin
from rsvp.models import Group, Guest
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum, Count


class GuestInline(admin.TabularInline):

    model = Guest
    fields = ('listed', 'name', 'age', 'table', 'attendance', 'diabetic', 'celiac',)


class GroupChangeList(ChangeList):

    def get_results(self, *args, **kwargs):
        super(GroupChangeList, self).get_results(*args, **kwargs)
        q = self.result_list.aggregate(count=Count('guests'))
        self.guests_count = q['count']
        q = self.result_list.filter(guests__attendance='Y').aggregate(count=Count('guests'))
        self.guests_attendance_yes = q['count']
        q = self.result_list.filter(guests__attendance='N').aggregate(count=Count('guests'))
        self.guests_attendance_no = q['count']


class GroupAdmin(admin.ModelAdmin):

    list_display = ('name', 'code', 'invited_by', 'guests_names', 'status', 'count', 'attendance', 'called', 'phone', 'comment',)
    inlines = (GuestInline,)
    list_filter = ('status', 'invited_by', 'called', 'web',)
    readonly_fields = ('updated',)
    search_fields = ('name', 'guests__name',)

    list_per_page = 1000
    list_max_show_all = 1000

    def get_changelist(self, request, **kwargs):
        return GroupChangeList

    def queryset(self, request):
        return super(GroupAdmin, self).queryset(request).prefetch_related('guests')


class GuestChangeList(ChangeList):

    def get_results(self, *args, **kwargs):
        super(GuestChangeList, self).get_results(*args, **kwargs)
        self.guests_count = self.result_list.count()
        self.guests_attendance_yes = self.result_list.filter(attendance='Y').count()
        self.guests_attendance_no = self.result_list.filter(attendance='N').count()


class GuestAdmin(admin.ModelAdmin):

    list_display = ('name', 'age', 'attendance', 'table', 'celiac', 'diabetic',)
    list_filter = ('listed', 'attendance', 'age', 'table', 'celiac', 'diabetic')
    readonly_fields = ('updated',)
    search_fields = ('name', 'group__name',)

    def get_changelist(self, request, **kwargs):
        return GuestChangeList

    def queryset(self, request):
        return super(GuestAdmin, self).queryset(request).prefetch_related('group')

admin.site.register(Group, GroupAdmin)
admin.site.register(Guest, GuestAdmin)