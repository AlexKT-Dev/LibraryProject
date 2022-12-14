from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import *
from .models import *


class UserDetailView(DetailView):
    model = UserModel
    context_object_name = 'user'
    template_name = 'user/user_detail.html'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = UserModel
    form_class = UserForm
    success_message = 'Successful creation'
    template_name = 'user/user_create_update.html'

    def get_success_url(self):
        return reverse_lazy('user:user_detail')


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = UserModel
    form_class = UserForm
    success_message = 'Successful change'
    template_name = 'user/user_create_update.html'

    def get_success_url(self):
        return reverse_lazy('user:user_detail')
