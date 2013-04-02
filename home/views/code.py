import json
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from home.views import GroupMixin
from django.template.loader import render_to_string
from django.template.context import RequestContext


class CodeView(View, GroupMixin):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CodeView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.POST.get('post', '{}'))
        group = self.get_group(request, data.get('code', None))
        if group:
            data = {
                'html': render_to_string('rsvp.html', { 'group': group }, RequestContext(request))
            }
        else:
            data = { 'invalid': True }
        response = HttpResponse(json.dumps(data), mimetype="application/json")
        self.set_group(response, group)
        return response
