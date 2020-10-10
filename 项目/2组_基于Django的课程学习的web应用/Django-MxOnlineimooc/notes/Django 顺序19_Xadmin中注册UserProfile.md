# Django 顺序19_Xadmin中注册UserProfile 以及修改密码 url BUG修复



### 传统做法：

卸载 Xadmin 中自动注册的 User，把自己的 UserProfile 注册进去。

在 extra_apps/xadmin/plugins/auth 下有 UserAdmin。Xadmin在其中已经定义好了 admin 的展示域等。

```python
class UserAdmin(object):
    change_user_password_template = None
    #...
```

但是 Xadmin 把 Django 的 User 与 Xadmin 自己的 UserAdmin 进行了关联。

```python
site.register(User, UserAdmin)
```



在自己的 apps/users/adminx.py 中先引入 UserAdmin，并继承 UserAdmin，仅需要 pass 即可。把 model 与 admin 关联起来。

```python
from xadmin.plugins.auth import UserAdmin

class UserProfileAdmin(UserAdmin):
    pass
```



## 实际做法：

### 1、把传统做法还原

目前项目中所用的包，并不需要把 model 与 admin 关联起来。因为 UserProfile 已经注册进去了，而且用户信息已经进去。

```python
xadmin.site.register(UserProfile, UserProfileAdmin)
```

也不需要卸载，比如：

```python
from django.contrib.auth.models import User
xadmin.site.unregister(User)
```

也不需要这一步

```python
from xadmin.plugins.auth import UserAdmin

class UserProfileAdmin(UserAdmin):
    pass
```



### 2、正确做法

只需要把这两行放在 extra_apps/xadmin/plugins/auth.py 中。

* 第一句，表示初始化的时候就去 settings 去查找 `AUTH_USER_MODEL`。
* 第二句，把 User 替换成自定义的 model。这样就可以把 UserProfile 注册进去。

```python
from django.contrib.auth import get_user_model
User = get_user_model()
```



因为 `get_user_model()` 会到 `auth/__init__.py` 中去找，找到 `try:` 就是在 settings 中取查找变量 `AUTH_USER_MODEL`。

```python
def get_user_model():
    """
    Returns the User model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.AUTH_USER_MODEL)
    except ValueError:
        raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "AUTH_USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL
        )
```



变量 `AUTH_USER_MODEL` 是我们在定义 `UserProfile` 的时候就在 settings 中配置好了的。

```python
AUTH_USER_MODEL = "users.UserProfile"
```



## 修改密码 url Bug

在extra_apps/xadmin/plugins/auth.py 中，最后的倒数第二行 url 需要修改成

```python
site.register_view(r'^users/userprofile/(.+)/password/$',
                   ChangePasswordView, name='user_change_password')
```

因为原来是另一个 url，导致显示不正常。

```python
site.register_view(r'^auth/user/(.+)/password/$',
                   ChangePasswordView, name='user_change_password')
```



















































