from django import forms
from django.forms import ModelForm
import datetime

from .models import Project, Task

class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['user',]

class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }