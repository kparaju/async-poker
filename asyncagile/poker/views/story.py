from django.views.generic import TemplateView, DetailView
from poker.models import Story

class StoryBrowse(TemplateView):
    template_name = 'story/browse.html'


class StoryDetails(DetailView):
    model = Story
    context_object_name = 'story'
    template_name = 'story/details.html'
