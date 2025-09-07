# notifications/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Notification

@login_required
def my_notifications(request):
    # 公告（receiver为空） + 当前用户的私人通知
    notifications = Notification.objects.filter(
        models.Q(receiver__isnull=True) | models.Q(receiver=request.user)
    ).order_by("-created_at")

    return render(request, "notifications/notifications.html", {"notifications": notifications})

@login_required
def mark_read(request, pk):
    """标记通知为已读"""
    notification = get_object_or_404(Notification, pk=pk, receiver=request.user)
    notification.is_read = True
    notification.save()
    return redirect("my_notifications")  # 跳回通知列表
