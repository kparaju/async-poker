from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, View
from poker.models import Story, Estimate, Project

class StoryBrowse(TemplateView):
    template_name = 'story/browse.html'


class StoryDetails(DetailView):
    model = Story
    context_object_name = 'story'
    template_name = 'story/details.html'


class StoryVote(DetailView):
    model = Story
    context_object_name = 'story'
    template_name = 'story/vote.html'


class EstimateNew(TemplateView):
    template_name = 'estimate/new.html'

    def get_context_data(self, **kwargs):
        context = super(EstimateNew, self).get_context_data(**kwargs)
        story = Story.objects.get(pk=kwargs['story'])
        estimate = Estimate.objects.filter(user=self.request.user).filter(story=story)
        if estimate:
            # redirect
            print "yes"

        context['story'] = story

        return context


class ProjectDetails(DetailView):
    template_name = 'project/details.html'
    model = Project
    context_object_name = 'project'
