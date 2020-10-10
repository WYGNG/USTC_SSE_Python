# -*- coding:utf-8 -*-

from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT

import xadmin

from users.views import IndexView, LoginView, LogoutView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView


urlpatterns = [
    # 处理 media 的访问，用于图片获取
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # 处理 static 的处理
    # url(r'^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),

    # xadmin 后台管理页面
    url(r'^xadmin/', xadmin.site.urls), # admin替换成xadmin

    # 主页
    url(r'^$', IndexView.as_view(), name='index'),

    # 用户登录页面
    url(r'^login/$', LoginView.as_view(), name='login'),

    # 用户退出页面
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    # 用户注册
    url(r'^register/$', RegisterView.as_view(), name='register'),

    # 验证码图片的路由
    url(r'^captcha/', include('captcha.urls')),

    # 用户注册：激活链接
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),

    # 找回密码页面
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),

    # 点击找回密码链接
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='rest_pwd'),

    # 点击找回密码链接
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    # 课程机构 url 配置
    url(r'^org/', include('organization.urls', namespace="org")),

    # 课程相关 url 配置
    url(r'^course/', include('courses.urls', namespace="course")),

    # 用户个人中心，放在 users app下
    url(r'^users/', include('users.urls', namespace='users')),

    # 富文本 Ueditor 相关 url
    # url(r'^ueditor/',include('DjangoUeditor.urls' )),



]

#全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'