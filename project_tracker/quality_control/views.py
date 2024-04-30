from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404, render, redirect
from .forms import BugReportForm, FeatureRequestForm
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


def create_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/quality_control/bugs/')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def create_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/quality_control/features/')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})


def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('/quality_control/bug_detail', project_id=bug_id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})

def update_feature(request, feature_id):
    feature = get_object_or_404(BugReport, pk=feature_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('/quality_control/feature_detail', project_id=feature_id)
    else:
        form = BugReportForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})

def delete_bug(request, bug_id):
    project = get_object_or_404(BugReport, pl=bug_id)
    project.delete()
    return redirect('/quality_control/bugs/')

def delete_feature(request, feature_id):
    project = get_object_or_404(FeatureRequest, pl=feature_id)
    project.delete()
    return redirect('/quality_control/features/')

# Class-Based Views
from django.views import View
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


from django.views.generic import ListView, CreateView, UpdateView, DeleteView


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




class BugCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name ='quality_control/bug_create.html'
    success_url = reverse_lazy('quality_control:bugs')

    def form_valid(self, form):
        form.instance.project = get_object_or_404(BugReport, pk=self.kwargs['bug_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('quality_control:bug_detail', kwargs={'bug_id':self.kwargs['bug_id']})



class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_create.html'
    success_url = reverse_lazy('quality_control:features')

    def form_valid(self, form):
        form.instance.project = get_object_or_404(FeatureRequest, pk=self.kwargs['feature_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('quality_control:feature_detail', kwargs={'feature_id':self.kwargs['feature_id']})




class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs')

    def get_success_url(self):
        return reverse_lazy('quality_control:bug_detail',
                            kwargs={'bug_id': self.object.id})


class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:features')

    def get_success_url(self):
        return reverse_lazy('quality_control:feature_detail',
                            kwargs={'feature_id': self.object.id})


class BugDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs')
    template_name = 'quality_control/bug_delete.html'

class FeatureDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:features')
    template_name = 'quality_control/feature_delete.html'