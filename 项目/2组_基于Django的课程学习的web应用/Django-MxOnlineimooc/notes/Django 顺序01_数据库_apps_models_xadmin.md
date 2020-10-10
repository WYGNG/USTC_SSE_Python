# Django 顺序1：数据库, apps, models, xadmin

## 本节的计划：

* 建立数据连接
* 搭建 apps 结构
* 建立 models
* 实现 xadmin 后台





## 测试 MySQL 连接

makemigration/migrate



## 建立 apps

### users

#### 自定义 auth_user (扩展该表)

**users.models.py**

继承 AbstractUser，并增加自己扩展的字段。

  ```python
  from django.contrib.auth.models import AbstractUser

  class UserProfile(AbstractUser):
      #...
  ```

注册 AUTH_USER_MODEL 到 settings.py 中

  ```python
  AUTH_USER_MODEL = "users.UserProfile"
  ```

如果 makemigrations/migrate users 报错：

```python
Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'.
```

则删除 users.migrations 中的 0001_initial.py，另外删除数据库内容，再 makemigrations/migrate users。



把 app 注册到 settings 中的 installed_apps。



### 把 app 放到一个文件下（apps）

项目中新建 package (自带`__init__.py` 文件)，把所有app拖入该目录下。

注意点：去掉 PyCharm 弹出警告框中的选项： Search for references。

让 Django 直接使用 apps 的名字，而不用类似于 apps.users 的包名。

1、PyCharm 中把 apps 右键 Mark Dictionary as > Source Root

2、settings.py 中把 apps 加入python的搜索目录下。

```python
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
```



### 设置 python 模板

Preferences / Editor / File and Code Templates / Python Script

```python
# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '$DATE $TIME'
```



### 把 models 注册到 xadmin 中

每个 apps 中建立 adminx.py 文件。

并把 xadmin 放入全局 urls

```python
# -*- coding:utf-8 -*-

from django.conf.urls import url
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
]
```





### xadmin的全局配置

放在一个 adminx.py 中，可以放 users 中

```python


# xadmin的配置
class BaseSetting():
    # 可以使用主题
    enable_themes = True
    # 使用bootswatch提供的主题
    use_bootswatch = True


class GlobalSettings():
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线网'
    menu_style = 'accordion'
    
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
```



配置每个 app 在 xadmin 中的显示名字，在每个 app  的目录下修改 apps.py。以Course 中的 apps.py 举例

```python
# coding:utf-8
from django.apps import AppConfig


class CoursesConfig(AppConfig):
    name = 'courses'
    verbose_name = "课程管理"
```

并在 Course 目录下的 `__init__.py` 中写入：

```python
default_app_config = "courses.apps.CoursesConfig"
```



## 静态文件处理

静态文件都放在项目目录下的 /static/ 目录中。

在 settings.py 中配置：

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

在模板中引用

```python
{% load staticfiles %}
```













