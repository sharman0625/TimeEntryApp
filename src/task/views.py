from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormMixin

from .models import Task, Project
from .forms import ProjectCreateForm, TaskCreateForm

# Create your views here.

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/')

class TaskView(ListView, FormMixin):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
        return redirect('/')