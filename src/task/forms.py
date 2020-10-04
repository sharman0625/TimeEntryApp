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
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date < datetime.datetime.now(start_date.tzinfo):
            self.add_error(None, forms.ValidationError('Start date or time must be greater than '+ str(datetime.datetime.now(start_date.tzinfo))))
        if end_date < start_date:
            self.add_error(None, forms.ValidationError('End date or time should be greater than start date.'))