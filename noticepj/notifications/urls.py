from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_notifications, name='my_notifications'),
    path('mark-read/<int:pk>/', views.mark_read, name='mark_read'),
]
