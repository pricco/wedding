from django.conf.urls import patterns
from home.views import IndexView
from home.views import CodeView
from home.views import ConfirmView

urlpatterns = patterns('',
    (r'^$', IndexView.as_view()),
    (r'^(?P<code>[a-zA-Z0-9]{3})/?$', IndexView.as_view()),
    (r'^(?P<code>[a-zA-Z0-9]{3})/card/?$', IndexView.as_view(mode='card')),
    (r'^(?P<code>[a-zA-Z0-9]{3})/rsvp/?$', IndexView.as_view(mode='rsvp')),
    (r'^(?P<code>[a-zA-Z0-9]{3})/map/?$', IndexView.as_view(mode='map')),
    (r'^code/?$', CodeView.as_view()),
    (r'^confirm/?$', ConfirmView.as_view()),
)