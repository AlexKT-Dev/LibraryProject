import os

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.conf import settings

from .forms import *
from .models import *


class BooksListView(ListView):
    model = BooksModel
    context_object_name = 'books'
    template_name = 'books/books_list.html'
    error_context = []

    def post(self, request, *args, **kwargs):
        if request.FILES:
            file = request.FILES['docs']
            fs = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'media/files'))
            fs.save(file.name, file)
        else:
            return 'Select file'
        return super().get(request)

    def download_file(self, dirname=''):
        if dirname:
            if os.path.exists(str(settings.MEDIA_ROOT) + '\\files\\'):
                return FileResponse(open(str(settings.MEDIA_ROOT) + '\\files\\'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        files = route_files_list()
        if files:
            context['files'] = files
        if self.error_context:
            context['error'] = self.error_context
        return context


class BooksDetailView(DetailView):
    model = BooksModel
    context_object_name = 'book'
    template_name = 'books/books_detail.html'


class BooksCreateView(SuccessMessageMixin, CreateView):
    model = BooksModel
    form_class = BooksForm
    success_message = 'Successful creation'
    template_name = 'books/books_create_update.html'

    def get_success_url(self):
        return reverse_lazy('books:books_list')


class BooksUpdateView(SuccessMessageMixin, UpdateView):
    model = BooksModel
    form_class = BooksForm
    success_message = 'Successful change'
    template_name = 'books/books_create_update.html'

    def get_success_url(self):
        return reverse_lazy('books:books_list')


class BooksDeleteView(SuccessMessageMixin, DeleteView):
    model = BooksModel
    success_message = 'Successful removal'

    def get_success_url(self):
        return reverse_lazy('books:books_list')


def route_files_list():
    files = None
    media_path = str(settings.MEDIA_ROOT) + '\\files\\'
    files = os.listdir(media_path)
    return files
