from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import BugReport, FeatureRequest
def index(request):
    bug_list = reverse('quality_control:bug_list')
    feature_list = reverse('quality_control:feature_list')
    html = (f"<h1>Страница контроля качества </h1><a href='{bug_list}'> <br> Список всех багов</a>"
            f"<br><a href='{feature_list}'> Запросы на улучшение</a>")
    return HttpResponse(html)



def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список багов</h1><ul>'
    for bug in bugs:
        bugs_html += f"<li><a href={bug.id}/>{bug.title}</a></li>"
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    feature_html = '<h1>Список багов</h1><ul>'
    for feature in features:
        feature_html += f"<li><a href={feature.id}/>{feature.title}</a></li>"
    feature_html += '</ul>'
    return HttpResponse(feature_html)

def bug_detail(request, bug_id):
    project = get_object_or_404(BugReport, id=bug_id)
    response_html = (f"<h1>{project.title}</h1>"
                     f"<br><aa>Description: {project.description}</aa>"
                     f"<br><bb>Created_at: {project.created_at}</bb>"
                     f"<br><cc>Priority: {project.priority:}</cc>"
                     f"<br><w>Projects: {project.project:}</w>"
                     f"<br><ee>Tasks: {project.task:}</ee>"
                     f"<br><p>Status: {project.status}</p>")
    response_html += '</ul>'
    return HttpResponse(response_html)

def feature_detail(request, feature_id):
    project = get_object_or_404(FeatureRequest, id=feature_id)
    response_html = (f"<h1>{project.title}</h1>"
                     f"<br><aa>Description: {project.description}</aa>"
                     f"<br><bb>Created_at: {project.created_at}</bb>"
                     f"<br><cc>Priority: {project.priority:}</cc>"
                     f"<br><w>Projects: {project.project:}</w>"
                     f"<br><ee>Tasks: {project.task:}</ee>"
                     f"<br><p>Status: {project.status}</p>")
    response_html += '</ul>'
    return HttpResponse(response_html)




# Class-Based Views
from django.views import View
class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list = reverse('quality_control:bug_list')
        feature_list = reverse('quality_control:feature_list')
        html = (f"<h1>Страница контроля качества </h1><a href='{bug_list}'> <br> Список всех багов</a>"
                f"<br><a href='{feature_list}'> Запросы на улучшение</a>")
        return HttpResponse(html)

from django.views.generic import ListView

class BugsListView(ListView):
    model = BugReport

    def get(self, request, *args, **kwargs):
        bugs = self.get_queryset()
        bugs_html = '<h1>Список багов</h1><ul>'
        for bug in bugs:
            bugs_html += f"<li><a href={bug.id}/>{bug.title}</a></li>"
        bugs_html += '</ul>'
        return HttpResponse(bugs_html)

class FeaturesListView(ListView):
    model = FeatureRequest

    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        feature_html = '<h1>Список багов</h1><ul>'
        for feature in features:
            feature_html += f"<li><a href={feature.id}/>{feature.title}</a></li>"
        feature_html += '</ul>'
        return HttpResponse(feature_html)

from django.views.generic import DetailView

class BugsDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        project = self.object
        response_html = (f"<h1>{project.title}</h1>"
                         f"<br><aa>Description: {project.description}</aa>"
                         f"<br><bb>Created_at: {project.created_at}</bb>"
                         f"<br><cc>Priority: {project.priority:}</cc>"
                         f"<br><w>Projects: {project.project:}</w>"
                         f"<br><ee>Tasks: {project.task:}</ee>"
                         f"<br><p>Status: {project.status}</p>")
        response_html += '</ul>'
        return HttpResponse(response_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        project = self.get_object()
        response_html = (f"<h1>{project.title}</h1>"
                         f"<br><aa>Description: {project.description}</aa>"
                         f"<br><bb>Created_at: {project.created_at}</bb>"
                         f"<br><cc>Priority: {project.priority:}</cc>"
                         f"<br><w>Projects: {project.project:}</w>"
                         f"<br><ee>Tasks: {project.task:}</ee>"
                         f"<br><p>Status: {project.status}</p>")
        response_html += '</ul>'
        return HttpResponse(response_html)
