from django.conf.urls import patterns
from home.views import IndexView

urlpatterns = patterns('',
    (r'^$', IndexView.as_view()),
    (r'^(?P<code>[a-zA-Z0-9]{3})/?$', IndexView.as_view()),
)