from django.views.generic import DetailView
from poker.models import Project

class ProjectDetails(DetailView):
    template_name = 'project/details.html'
    model = Project
    context_object_name = 'project'
