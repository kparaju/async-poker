from django.conf.urls import patterns, url
from poker import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'project/details/(?P<pk>[-_\w]+)',  login_required(views.ProjectDetails.as_view()), name='project-details'),
    url(r'story/browse/$',  login_required(views.StoryBrowse.as_view()), name='story-browse'),
    url(r'story/details/(?P<pk>[-_\w]+)',  login_required(views.StoryDetails.as_view()), name='story-details'),
    url(r'estimate/new/(?P<story>\w+)',  login_required(views.EstimateNew.as_view()), name='estimate-new'),
)
