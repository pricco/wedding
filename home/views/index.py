from django.views.generic import TemplateView
from music.models import Song
from location.models import Location

class IndexView(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        kwargs['songs'] = Song.objects.filter(active=True).order_by('order')
        kwargs['locations'] = Location.objects.filter(active=True)
        return super(IndexView, self).get(request, *args, **kwargs)