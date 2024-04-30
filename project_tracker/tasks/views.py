from django.http import HttpResponse
from django.urls import reverse
from .models import Project, Task
from .forms import FeedbackForm
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProjectForm

def index(request):
    return render(request,'tasks/index.html')

def projects_list(request):
    projects = Project.objects.all()
    return render(request,'tasks/projects_list.html', {'project_list':projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'tasks/project_detail.html', {'project':project})

def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project=project_id)
    return render(request, 'tasks/task_detail.html', {'task':task})

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks/projects')
    else:
        form = ProjectForm()
    return render(request, 'tasks/project_create.html', {'form': form})


from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')

from django.views.generic import ListView

class ProjectsListView(ListView):
    model = Project
    template = 'tasks/projects_list.html'


from django.views.generic import DetailView

class ProjectsDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'
    template = 'tasks/project_detail.html'

class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template = 'tasks/task_detail.html'
