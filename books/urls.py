from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),
    path('<int:pk>/', BooksDetailView.as_view(), name='books_detail'),
    path('create/', BooksCreateView.as_view(), name='books_create'),
    path('<int:pk>/edit/', BooksUpdateView.as_view(), name='books_update'),
    path('<int:pk>/delete', BooksDeleteView.as_view(), name='books_delete'),
]
