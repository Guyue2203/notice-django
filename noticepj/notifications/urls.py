from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_notifications, name='notifications_list'),
    path('mark-read/<int:pk>/', views.mark_read, name='mark_read'),
]
