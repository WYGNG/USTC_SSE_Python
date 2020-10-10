# -*- coding:utf-8 -*-
from django.apps import AppConfig
# 用于配置app显示名称

# 修改users显示为“用户信息”
class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = u"用户信息"
