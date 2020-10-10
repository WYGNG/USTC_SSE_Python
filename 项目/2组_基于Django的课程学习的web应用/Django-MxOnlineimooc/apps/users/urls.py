# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/9/17 12:01 PM'

from django.conf.urls import url

from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView
from .views import UpdateEmailView, MyCourseView, MyFavOrg, MyFavTeacherView, MyFavCourseView, MymessageView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),

    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),

    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),

    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

    # 我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),

    # 我收藏的课程机构
    url(r'^myfav/org/$', MyFavOrg.as_view(), name="myfav_org"),

    # 我收藏的授课讲师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),

    # 我收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),

    # 我收藏的课程
    url(r'^mymessage/$', MymessageView.as_view(), name="mymessage"),



]

