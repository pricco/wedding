from django.views.generic import TemplateView
from music.models import Song
from location.models import Location
from home.views import GroupMixin


class IndexView(TemplateView, GroupMixin):

    template_name = 'index.html'
    card = False

    def get(self, request, code=None, *args, **kwargs):
        group = self.get_group(request, code)
        kwargs['songs'] = Song.objects.filter(active=True).order_by('order', 'id')
        kwargs['locations'] = Location.objects.filter(active=True)
        kwargs['card'] = group and self.card
        kwargs['group'] = group
        response = super(IndexView, self).get(request, *args, **kwargs)
        self.set_group(response, group)
        return response

