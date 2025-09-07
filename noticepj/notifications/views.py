# notifications/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Notification

def my_notifications(request):
    """
    显示通知列表：
    - 未登录用户：只显示公告
    - 登录用户：显示公告 + 属于自己的私人通知
    """
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(
            Q(receiver=request.user) | Q(receiver=None)
        ).order_by("-created_at")
    else:
        notifications = Notification.objects.filter(receiver=None).order_by("-created_at")

    return render(request, "notifications/notifications_list.html", {
        "notifications": notifications
    })


@login_required
def mark_read(request, pk):
    """
    标记通知已读（只允许接收者自己标记）
    """
    notif = get_object_or_404(Notification, pk=pk)
    if notif.receiver == request.user:
        notif.is_read = True
        notif.save()
    return redirect('notifications_list')  # 返回通知列表
