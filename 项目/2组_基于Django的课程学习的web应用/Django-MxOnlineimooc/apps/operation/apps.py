# coding:utf-8
from django.apps import AppConfig

# 修改operation显示为“用户操作”
class OperationConfig(AppConfig):
    name = 'operation'
    verbose_name = "用户操作"
