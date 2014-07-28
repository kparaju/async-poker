from django.conf.urls import patterns, url
from poker import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'story/view/(?P<pk>[-_\w]+)',  login_required(views.StoryDetails.as_view()), name='view-story'),
)
