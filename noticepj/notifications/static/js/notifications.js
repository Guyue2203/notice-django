// 通知页面交互脚本

document.addEventListener('DOMContentLoaded', function() {
  // 为所有通知项添加鼠标悬停/点击微交互
  const notificationItems = document.querySelectorAll('.notification-item');
  
  if (notificationItems && notificationItems.length) {
    notificationItems.forEach(item => {
      item.addEventListener('click', function(e) {
        // 如果点击的是标记已读按钮，不执行此效果
        if (e.target.classList.contains('mark-read-btn') || 
            (e.target.closest && e.target.closest('.mark-read-btn'))) {
          return;
        }
        // 轻微点击效果
        this.style.transform = 'scale(0.98)';
        setTimeout(() => {
          this.style.transform = 'scale(1)';
        }, 150);
      });
    });
  }
  
  // 为标记已读按钮添加即时反馈
  const markReadBtns = document.querySelectorAll('.mark-read-btn');
  
  if (markReadBtns && markReadBtns.length) {
    markReadBtns.forEach(btn => {
      btn.addEventListener('click', function(e) {
        // 阻止事件冒泡，避免触发通知项的点击效果
        e.stopPropagation();
        
        const notificationItem = this.closest('.notification-item');
        if (notificationItem) {
          notificationItem.style.opacity = '0.75';
          notificationItem.style.backgroundColor = '#f8f9fa';
        }
        this.style.pointerEvents = 'none';
        this.style.opacity = '0.6';
      });
    });
  }
});