from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_notifications",
        null=True, blank=True   # 新增：允许为空
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_notifications",
        null=True, blank=True   # 仍然允许为空 → 公告
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        if self.receiver:
            return f"{self.sender.username if self.sender else '未知'} → {self.receiver.username}: {self.message[:20]}"
        return f"[公告] {self.sender.username if self.sender else '系统'}: {self.message[:20]}"

