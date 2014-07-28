from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, View
from poker.models import Story

def home(request):
    return ''
    if request.user and request.user.is_authenticated():
        return redirect(reverse('view-projects'))
    return render(request, 'landing.html')

class BaseView(TemplateView):
    template_name = 'base.html'

class StoryDetails(DetailView):
    model = Story
    context_object_name = 'story'
    template_name = 'story/details.html'
