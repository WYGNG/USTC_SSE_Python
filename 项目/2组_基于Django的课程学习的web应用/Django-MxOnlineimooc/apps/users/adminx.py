# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/11/19 11:06 AM'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import EmailVerifyRecord, Banner, UserProfile


# class UserProfileAdmin(UserAdmin):
#     def get_form_layout(self):
#         if self.org_obj:
#             self.form_layout = (
#                 Main(
#                     Fieldset('',
#                              'username', 'password',
#                              css_class='unsort no_title'
#                              ),
#                     Fieldset(_('Personal info'),
#                              Row('first_name', 'last_name'),
#                              'email'
#                              ),
#                     Fieldset(_('Permissions'),
#                              'groups', 'user_permissions'
#                              ),
#                     Fieldset(_('Important dates'),
#                              'last_login', 'date_joined'
#                              ),
#                 ),
#                 Side(
#                     Fieldset(_('Status'),
#                              'is_active', 'is_staff', 'is_superuser',
#                              ),
#                 )
#             )
#         return super(UserAdmin, self).get_form_layout()



# xadmin管理系统UI的配置
class BaseSetting():
    # 允许使用主题功能
    enable_themes = True
    # 使用bootswatch提供的主题
    use_bootswatch = False

# xadmin管理页面设置
class GlobalSettings():
    site_title = '慕学后台管理系统' # 顶部页头名称
    site_footer = '慕学在线网'     # 底部页脚名称
    # 每个 app 下 model 可以收缩起来
    menu_style = 'accordion'


# 添加model
class EmailVerifyRecordAdmin(): #
    list_display = ['code', 'email', 'send_type', 'send_time'] # 列表页显示的字段
    search_fields = ['code', 'email', 'send_type']             # 定义可以搜索的字段
    list_filter = ['code', 'email', 'send_type', 'send_time']
    model_icon = 'fa fa-address-book-o'

# 添加model
class BannerAdmin():
    list_display = ['title', 'image', 'url', 'index', 'add_time'] # 列表页显示的字段
    search_fields = ['title', 'image', 'url', 'index']            # 定义可以搜索的字段
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin) #注册EmailVerifyRecord表
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting) # 注册BaseSetting主题功能
xadmin.site.register(views.CommAdminView, GlobalSettings)


# xadmin.site.register(UserProfile, UserProfileAdmin)
# from django.contrib.auth.models import User
# xadmin.site.unregister(User)
