# notifications/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from .models import Notification

def home(request):
    """
    首页视图，提供管理后台和通知页面的入口
    """
    return render(request, "notifications/home.html")

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


@csrf_protect
@require_POST
def ajax_logout(request):
    """
    AJAX退出登录，清除会话并返回成功状态
    """
    logout(request)
    return JsonResponse({'success': True, 'message': '退出成功'})