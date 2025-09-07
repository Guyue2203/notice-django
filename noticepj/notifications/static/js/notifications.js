// 通知页面交互脚本

document.addEventListener('DOMContentLoaded', function() {
  // 为所有通知项添加鼠标悬停效果
  const notificationItems = document.querySelectorAll('.notification-item');
  
  notificationItems.forEach(item => {
    // 添加点击效果
    item.addEventListener('click', function(e) {
      // 如果点击的是标记已读按钮，不执行此效果
      if (e.target.classList.contains('mark-read-btn') || 
          e.target.closest('.mark-read-btn')) {
        return;
      }
      
      // 添加轻微的点击效果
      this.style.transform = 'scale(0.98)';
      setTimeout(() => {
        this.style.transform = 'scale(1)';
      }, 150);
    });
  });
  
  // 为标记已读按钮添加确认功能
  const markReadBtns = document.querySelectorAll('.mark-read-btn');
  
  markReadBtns.forEach(btn => {
    btn.addEventListener('click', function(e) {
      // 阻止事件冒泡，避免触发通知项的点击效果
      e.stopPropagation();
      
      // 获取通知项
      const notificationItem = this.closest('.notification-item');
      
      // 添加已读效果
      notificationItem.style.opacity = '0.6';
      notificationItem.style.backgroundColor = '#f8f9fa';
      
      // 隐藏按钮
      this.style.display = 'none';
    });
  });
});