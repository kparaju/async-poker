from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from poker.views.estimate import EstimateNew
from poker.views.project import ProjectDetails
from poker.views.story import StoryBrowse, StoryDetails

urlpatterns = patterns('',
    url(r'project/details/(?P<pk>[-_\w]+)',  login_required(ProjectDetails.as_view()), name='project-details'),
    url(r'story/browse/$',  login_required(StoryBrowse.as_view()), name='story-browse'),
    url(r'story/details/(?P<pk>[-_\w]+)',  login_required(StoryDetails.as_view()), name='story-details'),
    url(r'estimate/new/(?P<story>\w+)',  login_required(EstimateNew.as_view()), name='estimate-new'),
)
