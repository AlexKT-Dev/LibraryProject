from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<pk>/edit/', UserUpdateView.as_view(), name='user_update')
]
