# Django 顺序15_用户登出功能

退出没有页面。用户退出后直接跳转到首页。



## 逻辑

Django 的 logout 方法、重定向方法、反向解析 url 方法

```python
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
```

逻辑实现：

* logout() 方法传入 request 作为参数
* 用户登出后使用重定向方法 HttpResponseRedirect() 传入的是 url 作为参数
* reverse("index") 方法是传入 url 的 name ，反向解析出该 name 对应的 url 地址

```python
class LogoutView(View):
    """
    用户退出（登出）
    """
    def get(self, request):
        logout(request)
        # 登出后重定向，另外直接使用页面的 name
        return HttpResponseRedirect(reverse("index"))
```



## 路由

```python
from users.views import LogoutView

urlpatterns = [
  url(r'^logout/$', LogoutView.as_view(), name="logout"),
]
```



## 模板

```python
<a class="fr" href="{% url 'logout' %}">退出</a>
```



























