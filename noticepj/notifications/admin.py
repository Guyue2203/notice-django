# notifications/admin.py
from django import forms
from django.contrib import admin
from django.utils import timezone
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """通知管理后台配置"""
    
    # 基础配置
    readonly_fields = ('created_at',)
    
    def get_fields(self, request, obj=None):
        """控制字段显示：新建时隐藏sender字段，公告时隐藏is_read字段"""
        fields = list(super().get_fields(request, obj))
        
        # 新建时隐藏sender字段（自动设置为当前用户）
        if obj is None and 'sender' in fields:
            fields.remove('sender')
        
        # 编辑时如果是公告（receiver为空），隐藏is_read字段
        if obj is not None and obj.receiver is None and 'is_read' in fields:
            fields.remove('is_read')
        
        return fields
    
    # 列表页面配置
    list_display = ('id', 'sender', 'receiver', 'message', 'is_read', 'formatted_created_at')
    list_filter = ('is_read', 'created_at', 'sender')
    search_fields = ('message', 'sender__username', 'receiver__username')
    
    # 静态文件配置
    class Media:
        js = ('js/notification_admin.js',)
    
    # 显示方法
    def formatted_created_at(self, obj):
        """格式化创建时间显示"""
        if obj.created_at:
            local_time = timezone.localtime(obj.created_at)
            return local_time.strftime('%Y年%m月%d日 %H:%M')
        return '-'
    
    formatted_created_at.short_description = '创建时间'
    formatted_created_at.admin_order_field = 'created_at'
    
    # 数据保存处理
    def save_model(self, request, obj, form, change):
        """新建时自动设置发送者为当前用户"""
        if not change:
            obj.sender = request.user
        super().save_model(request, obj, form, change)
    
    # 权限控制
    def has_change_permission(self, request, obj=None):
        """只有超级用户或发送者本人可以修改通知"""
        if obj is None:
            return True
        return request.user.is_superuser or obj.sender == request.user
    
    def has_delete_permission(self, request, obj=None):
        """只有超级用户或发送者本人可以删除通知"""
        if obj is None:
            return True
        return request.user.is_superuser or obj.sender == request.user