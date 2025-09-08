# 通知系统 (Notice Django)

## 项目简介

这是一个基于Django框架开发的通知推送平台，支持公告发布和私人通知功能。系统提供了用户友好的Web界面和强大的管理后台，为后续其他项目的开展提供技术上的借鉴支持。

### 主要功能

- **公告系统**：支持发布公开公告，所有用户可见
- **私人通知**：支持用户间发送私人通知
- **用户认证**：集成Django用户认证系统
- **管理后台**：提供完整的通知管理功能
- **响应式设计**：支持移动端和桌面端访问
- **实时交互**：支持AJAX操作和动态UI更新

## 技术栈

- **后端框架**：Django 5.2.6
- **数据库**：SQLite3（开发环境）
- **前端技术**：HTML5、CSS3、JavaScript
- **UI组件**：Bootstrap Icons
- **认证系统**：Django内置用户认证

## 项目架构

```
noticepj/                     # 项目根目录
├── manage.py                  # Django管理入口（运行、迁移、创建用户等）
├── db.sqlite3                 # SQLite数据库文件
├── noticepj/                  # 主配置目录
│   ├── __init__.py
│   ├── settings.py            # 全局配置文件（数据库/APP/中间件等）
│   ├── urls.py                # 全局URL路由配置
│   ├── asgi.py                # 异步服务入口（WebSocket用）
│   └── wsgi.py                # 同步服务入口（Gunicorn/Nginx用）
│
├── notifications/             # 通知应用模块
│   ├── __init__.py
│   ├── admin.py               # Django Admin后台配置
│   ├── apps.py                # 应用配置
│   ├── models.py              # 数据模型（Notification）
│   ├── views.py               # 视图函数（首页、通知列表、标记已读等）
│   ├── urls.py                # 应用级URL路由
│   ├── tests.py               # 单元测试
│   ├── migrations/            # 数据库迁移文件
│   │   ├── __init__.py
│   │   ├── 0001_initial.py    # 初始迁移
│   │   └── 0002_rename_content_notification_message_and_more.py
│   ├── templates/             # HTML模板目录
│   │   ├── notifications/
│   │   │   ├── home.html      # 首页模板
│   │   │   └── notifications_list.html  # 通知列表模板
│   │   └── registration/
│   │       └── login.html     # 登录页面模板
│   └── static/                # 静态文件目录
│       ├── css/
│       │   ├── notifications.css    # 自定义样式
│       │   └── bootstrap-icons.css  # Bootstrap图标
│       ├── js/
│       │   └── notifications.js     # 前端交互脚本
│       └── admin/
│           └── js/
│               └── notification_admin.js  # 管理后台脚本
```

## 数据模型

### Notification（通知模型）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | BigAutoField | 主键，自增ID |
| sender | ForeignKey(User) | 发送者，可为空（系统公告） |
| receiver | ForeignKey(User) | 接收者，可为空（公开公告） |
| message | TextField | 通知内容 |
| created_at | DateTimeField | 创建时间，自动设置 |
| is_read | BooleanField | 是否已读，默认False |

## URL路由

### 全局路由 (noticepj/urls.py)
- `/` - 首页（通知系统入口）
- `/admin/` - Django管理后台
- `/notifications/` - 通知应用路由
- `/accounts/` - 用户认证路由

### 通知应用路由 (notifications/urls.py)
- `/notifications/` - 通知列表页面
- `/notifications/mark-read/<id>/` - 标记通知已读
- `/notifications/ajax-logout/` - AJAX退出登录

## 功能特性

### 1. 首页功能
- 提供通知页面和管理后台的入口
- 响应式设计，支持移动端
- 现代化UI设计

### 2. 通知系统
- **公告功能**：管理员可发布公开公告
- **私人通知**：用户间可发送私人通知
- **权限控制**：未登录用户只能查看公告
- **已读标记**：支持标记私人通知为已读
- **实时更新**：支持AJAX操作

### 3. 管理后台
- 完整的通知管理界面
- 支持创建、编辑、删除通知
- 智能字段显示（根据通知类型动态调整）
- 权限控制（只有发送者或超级用户可修改）
- 时间格式化显示

### 4. 用户认证
- 集成Django用户认证系统
- 支持用户登录/退出
- 登录状态显示
- 登录重定向功能

## 安装和运行

### 环境要求
- Python 3.8+
- Django 5.2.6

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd notice-django
   ```

2. **安装依赖**
   ```bash
   pip install django
   ```

3. **数据库迁移**
   ```bash
   python manage.py migrate
   ```

4. **创建超级用户**
   ```bash
   python manage.py createsuperuser
   ```

5. **启动开发服务器**
   ```bash
   python manage.py runserver
   ```

6. **访问应用**
   - 首页：http://127.0.0.1:8000/
   - 通知页面：http://127.0.0.1:8000/notifications/
   - 管理后台：http://127.0.0.1:8000/admin/

## 使用说明

### 管理员操作
1. 访问管理后台创建用户
2. 发布公告或发送私人通知
3. 管理现有通知

### 普通用户操作
1. 注册/登录账户
2. 查看公告和私人通知
3. 标记私人通知为已读

## 开发说明

### 数据库迁移历史
- `0001_initial.py`：创建初始Notification模型
- `0002_rename_content_notification_message_and_more.py`：重构模型，添加sender字段，支持公告功能

### 静态文件配置
- 静态文件目录：`notifications/static/`
- 支持CSS、JavaScript和图片资源
- 使用Django静态文件服务

### 模板系统
- 使用Django模板语言
- 支持模板继承和包含
- 响应式设计

## 扩展建议

1. **功能扩展**
   - 添加通知分类功能
   - 支持富文本编辑器
   - 添加通知推送功能
   - 支持文件附件

2. **技术优化**
   - 添加Redis缓存
   - 使用PostgreSQL数据库
   - 添加API接口
   - 支持WebSocket实时通知

3. **部署优化**
   - 使用Docker容器化
   - 配置Nginx反向代理
   - 添加HTTPS支持
   - 设置日志监控

## 许可证

本项目仅供学习和参考使用。