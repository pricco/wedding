import json
from django.views.generic import View
from rsvp.models import Group
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.template.context import RequestContext
from django.template.loader import render_to_string
from home.views import GroupMixin


class ConfirmView(View, GroupMixin):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ConfirmView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        confirmed = False
        group = self.get_group(request)
        data = json.loads(request.POST.get('post', '{}'))
        if group and data:
            if 'message' in data:
                group.message = data['message']
            if 'guests' in data:
                for guest in group.guests.all():
                    dguest = next(iter(filter(lambda g: g['id'] == guest.id, data.get('guests', []))), None)
                    if dguest:
                        if 'attendance' in dguest:
                            guest.attendance = (dguest['attendance'] and 'Y') or 'N'
                        if 'celiac' in dguest:
                            guest.celiac = dguest['celiac']
                        guest.save()
            group.web = True
            group.save()
            confirmed = True
        return HttpResponse(json.dumps({
            'confirmed': confirmed,
            'html': render_to_string('rsvp.html', {
                'group': group }, RequestContext(request))
        }), mimetype="application/json")
