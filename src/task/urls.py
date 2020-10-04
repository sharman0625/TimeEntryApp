from django.urls import path

from .views import TaskView, ProjectCreateView

urlpatterns = [
    path('', TaskView.as_view(), name='home'),
    path('add-project/', ProjectCreateView.as_view(), name='add-project'),
]