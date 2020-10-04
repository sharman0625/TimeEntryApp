from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def get_all_tasks(self):
        tasks = Task.objects.filter(project=self)
        return tasks

class Task(models.Model):
    title = models.CharField(max_length=30)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def get_project(self):
        return self.project.name