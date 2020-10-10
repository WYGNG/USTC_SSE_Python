# Django 顺序10_用户登录权限的认证



目的：对用户的是否登录进行认证。只有登录的用户才能进行某些操作，比如评论与开始学习。



## 函数的登录认证

如果 views 是一个函数，可以使用装饰器

```python
@login_required
def AnyView(request):
    #...
```



## 自定义类的登录认证

如果是一个类，需要继承基础类。这个基础类是自己写的，放在 apps.utils.mixin_utils.py 中

```python
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
```

`dispatch` 函数，必须用这个名词，而且后面的参数也要如此。

Django 装饰器，如果用户未登录状态，就会自动跳转到 `/login/`。这里做了登录与否的认证。

```python
@method_decorator(login_required(login_url='/login/'))
```

Mixin 结尾的函数或者类代表了基础的函数或者类。



## 使用类的登录认证

在courses.views.py中引入，让评论逻辑的类同时继承该认证类与 View 类，且认证类必须在前。

表示必须登录，才能用这两个 views 逻辑进行处理，否则跳转到登录页面。

```python
from utils.mixin_utils import LoginRequiredMixin


class ComentsView(LoginRequiredMixin, View):
    #...
    
class CourseInfoView(LoginRequiredMixin, View):
    #...
```



自此，保证了学习与评论逻辑中，可以取出对应的登录用户。



















