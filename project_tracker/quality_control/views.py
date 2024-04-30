from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import BugReport, FeatureRequest

def index(request):
    return render(request, 'quality_control/index.html')



def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})



def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})


# Class-Based Views
from django.views import View
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


from django.views.generic import ListView

class BugsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_list.html'


class FeaturesListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'


from django.views.generic import DetailView

class BugsDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'