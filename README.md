# 说明文档

## 基本信息

该项目的目标是实现一个通知推送平台的搭建，为后续其他项目的开展提供技术上的借鉴支持。

该项目基于django框架搭建。



## 项目架构

noticepj/                     # 项目根目录
├── manage.py                  # 管理入口（运行、迁移、创建用户等）
├── noticepj/                  # 主配置目录（同名文件夹）
│   ├── __init__.py
│   ├── settings.py            # 全局配置文件（数据库/APP/中间件等）
│   ├── urls.py                # 全局 URL 路由
│   ├── asgi.py                # 异步服务入口（WebSocket 用）
│   └── wsgi.py                # 同步服务入口（Gunicorn/Nginx 用）
│
├── notifications/             # 自建 APP：负责通知逻辑
│   ├── __init__.py
│   ├── admin.py               # Django Admin 后台配置
│   ├── apps.py
│   ├── migrations/            # 数据库迁移记录
│   │   └── __init__.py
│   ├── models.py              # 数据表结构（Notification 等）
│   ├── views.py               # 视图函数（展示通知/接口）
│   ├── urls.py                # APP 级别 URL（如 /notifications/）
│   ├── templates/             # 前端模板目录
│   │   └── notifications/
│   │       └── notifications.html
│   └── static/                # 静态文件目录（css/js/img）
│
├── db.sqlite3                 # 默认数据库（开发环境）
└── requirements.txt           # 项目依赖（建议手动生成）



