from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView, FormView
from django.views.generic.edit import FormMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Task, Project, Customer
from .forms import ProjectCreateForm, TaskCreateForm, UserRegisterationForm

# Create your views here.

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterationForm
    success_url = 'task/login.html'
    template_name = 'task/signup.html'
    # success_message = f"%{username} was created successfully"

    def form_valid(self, form):
        user = form.save()
        first_name = form.cleaned_data.get('first_name')     
        last_name = form.cleaned_data.get('last_name')
        Customer.objects.create(user=user, first_name=first_name, last_name=last_name)
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'task/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return redirect("login")
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect("login")

        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer
        form.save()
        return redirect('/')

class TaskView(ListView, FormMixin):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task/index.html'

    def get_form_kwargs(self):
        kwargs = super(TaskView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get(user=self.request.user)
        context['projects'] = Project.objects.filter(customer=customer)
        context['count'] = Project.objects.filter(customer=customer).count()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
        return redirect('/')