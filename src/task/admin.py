from django.contrib import admin

from .models import Project, Task, Customer

# Register your models here.

admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Task)