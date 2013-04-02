from rsvp.models import Group


class GroupMixin():

    def get_group(self, request, code=None):
        code = (code and code.upper()) or request.get_signed_cookie('code', default=None, salt='wedding') or None
        group = None
        if code:
            try:
                group = Group.objects.get(code=code)
            except Group.DoesNotExist:
                pass
        return group

    def set_group(self, response, group):
        response.set_signed_cookie('code', value=group and group.code, salt='wedding')