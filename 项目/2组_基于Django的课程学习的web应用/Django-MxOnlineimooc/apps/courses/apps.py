# coding:utf-8
from django.apps import AppConfig

# 修改courses显示为“课程管理”
class CoursesConfig(AppConfig):
    name = 'courses'
    verbose_name = "课程管理"
