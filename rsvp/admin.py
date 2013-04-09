from django.contrib import admin
from rsvp.models import Group, Guest
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum, Count, Q


class GuestInline(admin.TabularInline):

    model = Guest
    ordering = ('order', 'id',)
    fields = ('order', 'name', 'alias', 'age', 'attendance', 'table', 'diabetic', 'celiac',)


class GroupChangeList(ChangeList):

    def get_results(self, *args, **kwargs):
        super(GroupChangeList, self).get_results(*args, **kwargs)
        stats = {
            'total': 0,
            'Y': {'A': 0, 'C': 0, 'B': 0, 'total': 0},
            'N': {'A': 0, 'C': 0, 'B': 0, 'total': 0},
            'U': {'A': 0, 'C': 0, 'B': 0, 'total': 0},
            'A': {'U': 0, 'Y': 0, 'N': 0, 'total': 0},
            'C': {'U': 0, 'Y': 0, 'N': 0, 'total': 0},
            'B': {'U': 0, 'Y': 0, 'N': 0, 'total': 0},
        }
        for value in self.result_list.values('guests__age', 'guests__attendance').annotate(count=Count('guests')):
            stats['total'] += value['count']
            stats[value['guests__attendance']]['total'] += value['count']
            stats[value['guests__attendance']][value['guests__age']] += value['count']
            stats[value['guests__age']]['total'] += value['count']
            stats[value['guests__age']][value['guests__attendance']] += value['count']
        self.stats = stats


class GroupAdmin(admin.ModelAdmin):

    list_display = ('name', 'code', 'invited_by', 'count', 'attendance', 'guests_names', 'status', 'comment', 'message',)
    inlines = (GuestInline,)
    list_filter = ('status', 'invited_by', 'called', 'web',)
    readonly_fields = ('updated',)
    search_fields = ('name', 'guests__name',)
    ordering = ('name',)

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

    list_display = ('name', 'alias', 'age', 'attendance', 'table', 'celiac', 'diabetic',)
    list_filter = ('attendance', 'age', 'table', 'celiac', 'diabetic')
    readonly_fields = ('updated',)
    search_fields = ('name', 'alias', 'group__name',)
    ordering = ('name',)

    list_per_page = 1000
    list_max_show_all = 1000

    def get_changelist(self, request, **kwargs):
        return GuestChangeList

    def queryset(self, request):
        return super(GuestAdmin, self).queryset(request).prefetch_related('group')

admin.site.register(Group, GroupAdmin)
admin.site.register(Guest, GuestAdmin)