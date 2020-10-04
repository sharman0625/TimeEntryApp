from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import TaskView, ProjectCreateView, RegisterView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', login_required(TaskView.as_view()), name='home'),
    path('add-project/', login_required(ProjectCreateView.as_view()), name='add-project'),
]