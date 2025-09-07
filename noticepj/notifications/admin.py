# notifications/admin.py
from django.contrib import admin
from django.utils import timezone
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'message', 'is_read', 'formatted_created_at')
    list_filter = ('is_read', 'created_at', 'sender')
    search_fields = ('message', 'sender__username', 'receiver__username')
    readonly_fields = ('sender', 'created_at')  # 发送者和创建时间设为只读
    
    class Media:
        js = ('admin/js/notification_admin.js',)
    
    def formatted_created_at(self, obj):
        """格式化创建时间显示"""
        if obj.created_at:
            # 转换为本地时间并格式化
            local_time = timezone.localtime(obj.created_at)
            return local_time.strftime('%Y年%m月%d日 %H:%M')
        return '-'
    formatted_created_at.short_description = '创建时间'
    formatted_created_at.admin_order_field = 'created_at'
    
    def get_readonly_fields(self, request, obj=None):
        """
        根据用户权限设置只读字段
        """
        if obj is None:  # 新建时
            # 新建时，只显示创建时间为只读，sender字段隐藏
            return ['created_at']
        else:  # 编辑时
            # 编辑时，发送者和创建时间都不可修改
            return ['sender', 'created_at']
    
    def get_fields(self, request, obj=None):
        """
        自定义字段显示，新建时隐藏sender字段
        """
        if obj is None:  # 新建时
            # 新建时隐藏sender字段，因为会自动设置为当前用户
            fields = list(super().get_fields(request, obj))
            if 'sender' in fields:
                fields.remove('sender')
            return fields
        else:  # 编辑时
            # 编辑时显示所有字段
            return super().get_fields(request, obj)
    
    def get_form(self, request, obj=None, **kwargs):
        """
        自定义表单，根据通知类型动态显示字段
        """
        form = super().get_form(request, obj, **kwargs)
        
        # 如果是编辑现有通知
        if obj is not None:
            # 如果是公告（receiver为None），隐藏is_read字段
            if obj.receiver is None:
                if 'is_read' in form.base_fields:
                    del form.base_fields['is_read']
        
        return form
    
    def save_model(self, request, obj, form, change):
        """
        保存时自动设置发送者为当前用户
        """
        if not change:  # 新建时
            obj.sender = request.user
        super().save_model(request, obj, form, change)
    
    def has_change_permission(self, request, obj=None):
        """
        只有超级用户或发送者本人可以修改通知
        """
        if obj is None:
            return True
        return request.user.is_superuser or obj.sender == request.user
    
    def has_delete_permission(self, request, obj=None):
        """
        只有超级用户或发送者本人可以删除通知
        """
        if obj is None:
            return True
        return request.user.is_superuser or obj.sender == request.user

