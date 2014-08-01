from django.views.generic import TemplateView
from poker.models import Story, Estimate

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
