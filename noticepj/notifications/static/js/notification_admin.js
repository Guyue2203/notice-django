// notification_admin.js
// 动态控制通知管理后台的字段显示

(function() {
    'use strict';
    
    // 等待jQuery加载完成
    function waitForJQuery(callback) {
        if (typeof django !== 'undefined' && django.jQuery) {
            callback(django.jQuery);
        } else if (typeof $ !== 'undefined') {
            callback($);
        } else {
            setTimeout(function() {
                waitForJQuery(callback);
            }, 100);
        }
    }
    
    function toggleIsReadField($) {
        var receiverField = $('#id_receiver');
        var isReadField = $('.field-is_read');
        
        if (receiverField.length && isReadField.length) {
            if (receiverField.val() === '' || receiverField.val() === null) {
                // 如果没有选择接收者（公告），隐藏is_read字段
                isReadField.hide();
            } else {
                // 如果选择了接收者（私人通知），显示is_read字段
                isReadField.show();
            }
        }
    }
    
    // 等待jQuery加载完成后执行
    waitForJQuery(function($) {
        $(document).ready(function() {
            // 页面加载时检查
            toggleIsReadField($);
            
            // 当receiver字段改变时检查
            $('#id_receiver').on('change', function() {
                toggleIsReadField($);
            });
        });
    });
    
})();
