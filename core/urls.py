from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # htmx
    path('add-task/', views.add_task, name='add_task'),
    path('delete-task/<str:pk>/', views.delete_task, name='delete_task'),
    path('edit-task/<str:pk>/', views.edit_task, name='edit_task'),
    path('check-title/', views.check_title, name='check_title'),
]