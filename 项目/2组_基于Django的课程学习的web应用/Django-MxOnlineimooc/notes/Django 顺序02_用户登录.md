# Django 顺序2：用户登录



## 用户登录逻辑

### index

把 index.html 放入 templates 目录中。

配置 urls

```python
#...
from django.views.generic import TemplateView

urlpatterns = [
	#...
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index')
]
```



#### 处理模板及静态文件：

1、引入静态文件

```html
{% load staticfiles %}
```

2、模板中引用

```python
src="{% static 'images/top_down.png' %}"
```



#### 登录逻辑处理

urls

```python
# -*- coding:utf-8 -*-

from users.views import login


urlpatterns = [
    #...

    # 用户登录页面
    url(r'^login/$', login, name='login'),  
]
```



users.views

```python
# coding:utf-8

from django.shortcuts import render
def login(request):
    # POST 要大写
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render(request, 'index.html', {})
```



#### django 从 request.POST 中获取用户名与密码

```python
		user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
```



#### 认证方法 authenticate

```python
from django.contrib.auth import authenticate


user = authenticate(username=user_name, password=pass_word)
```

anthenticate 传入两个参数 username和密码，如果认证成功会返回user的model的对象，如果失败返回 None。

这里 authenticate 参数名称必须写明 username= , password = 

```python
user = authenticate(username=user_name, password=pass_word)
```





判断用户认证成功后，调用login，传入 request, user两个参数。跳转到首页。

```python
        if user is not None:
            login(request, user)
            return render(request, "index.html")
```



### 模板中判断是否登录 request.user.is_authenticated

用于修改首页修改右上角的头

```python
            {% if request.user.is_authenticated %}
                <!--登录后跳转-->
        	{% else %}
                <!--登录前-->
            {% endif %}
```



### 修正两个 bug: authenticate参数 与 login 函数名

 authenticate 参数名称必须写明 username= , password = 

```python
user = authenticate(username=user_name, password=pass_word)
```

views 的 login 函数名称不能和 django 的 login 函数重名

```python
def user_login(request):
```

urls

```python
url(r'^login/$', user_login, name='login'),
```



### 自定义 authenticate() 1：初步实现自定义

在 user.views 中自定义 authenticate 方法（重载），这里是只考虑传入用户名和密码的情况。

成功就返回 user 对象，否则返回 None。因为 .objects.get() 方法没有查到或者多于一个，就会抛异常。

这里只用用户名与密码，先检测是否能够自定义成功。

```python
# 自定义 authenticate 实现邮箱登录
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 查找用户在 model 中是否存在，用 get 可以确保只有一个该用户
            user = UserProfile.objects.get(username=username)
            # 传入的密码，与 model 中的对比，只能使用 check_password 方法
            if user.check_password(password):
                return user
        except Exception as e:
            return None
```





settings.py 中增加一个元组（第一个元素后面需要加逗号），帮刚才自定义的方法传进去：

```python
# Application definition
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)
```

调试可以进入。



### 自定义 authenticate() 2：实现邮箱登录

核心点在于用户传入的参数是：用户名 或者 邮箱。所以查询数据（model）的时候，也需要查询 用户 或者 邮箱。

因此这里查询数据库是，就要用并集。会用到 .objects.get() 的 `Q()` 方法。

在 `.objects.get()` 的参数中，有 `Q()` 语法。

* 并集：`Q(username=username) | Q(email=username)` 就是用户传入的参数username，查用户名与邮箱的并集。
* 交集：`Q(username=username), Q(password=password)` 就是查交集
* 并集与交集级联 `Q(username=username) | Q(email=username), Q(password=password)`

改写 authenticate 的内容

```python
# 自定义 authenticate 实现邮箱登录
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 查找用户在 model 中是否存在，用 get 可以确保只有一个该用户
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            # 传入的密码，与 model 中的对比，只能使用 check_password 方法
            if user.check_password(password):
                return user
        except Exception as e:
            return None
```



### 返回登录错误信息

#### 认证不通过

首先对客户验证，验证不通过会传递错误信息 msg 回去。

```python
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
    	if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html", {"msg":"用户名或密码错误"})
```

msg 传模板。一旦有错误信息，就会显示出来。

```html
			<div class="error btns login-form-tips" id="jsLoginTips">
            {{ msg }}
          </div>
```



### 用类的方法取代函数方法写 views.py 中的逻辑

之前的函数方法是：

```python
def user_login(request):
    # POST 要大写
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html", {"msg":"用户名或密码错误"})
        pass
    elif request.method == 'GET':
        return render(request, 'login.html', {})
```

对应 urls

```python
from users.views import user_login

urlpatterns = [
    #...
    url(r'^login/$', user_login, name='login'),
]
```

可以替换成类方法：

```python
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误"})
        pass
```

这里改成 `LoginView.as_view()` 方法，

```python
from users.views import LoginView

urlpatterns = [
    #...
    url(r'^login/$', LoginView.as_view(), name='login'),
]
```



### 用 Django 的 forms 做表单验证

表单验证的好处是，仅需要配置就可以进行大量的表单验证以及错误提示工作，并不需要自己去写错误判断逻辑。

首先，在 users 目录下建立  forms.py 文件。LoginForm 继承 forms.Form，其中两个字段都是 CharField 类型，而且都是必填字段，密码要求最小5个字。

```python
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
```

然后，将该 LoginForm 引入到 views 中。在 views 去获取 request.POST 中的内容（比如 username 与 password）以前，先用 form 去做表单验证。

具体做法：

* 将 LoginForm 实例化
* 传入的参数必须是字典类型，所以传入 request.POST。但是这里需要注意 html 中每个 input 的 name 属性的值，必须和 form 中的字段名保持一致。
* `.is_valid()` 方法做表单验证。

```python
from .forms import LoginForm

class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            pass  # 处理表单验证成功后的逻辑
        #...
```

把刚才的逻辑加进来，实现用 form 首先去做表单验证是否输入符合规则。原来的用户认证，放在表单验证之后去做。

```python
class LoginView(View):
        def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误"})
```



### 表单验证错误信息返回模板

关键点：直接把 form 传回模板，模板中调用 form 中的错误信息，并显示出来。

html 调用 form 的错误信息以后，有两种常用用法。一是判断有无错误，并对错误的 input 位置加上警告框。二是把错误直接显示出来。

#### 1. 判断有无错误，做对应的警告框

form 结构其实类似于字典。当 form 验证出错时，form.errors 就不再是空值，而是出现对应的字段。比如：如果用户名（字段名 username）出错，就会有 form.errors.username。

所以在模板中就可以对该值进行判断，一旦某字段有错，可以实现对该字段高亮显示（结合 CSS 属性）：

```html
<div class="form-group marb20 {% if login_form.errors.username %}errorput{% endif %}">
    <input name="username" id="username" type="text" placeholder="手机号/邮箱"/>
</div>
```

#### 2. 显示 form 中的错误信息

errors是一个字典，所以对字典遍历时，一是要用 字典.items，而是同时在前面对 键和值 进行遍历：

```html
<div class="error btns login-form-tips" id="jsLoginTips">
    {% for key, error in login_form.errors.items %}{{ key }}:{{ error }}{% endfor %}
</div>
```

当然可以只显示错误

```html
<div class="error btns login-form-tips" id="jsLoginTips">
    {% for key, error in login_form.errors.items %}{{ key }}{% endfor %}
</div>
```



### 分开 表单验证、用户认证 的逻辑

流程，逐步往下：

* 表单验证：错误则返回表单中的错误信息，要求用户重新输入登录信息。
* 用户验证：错误则返回“用户名或密码错误”信息，要求用户重新输入登录信息。
* 表单合格、验证通过：进行用户登录。

```python
class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html",{"msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"login_form":login_form})
```



### 完善：登陆后跳转

用户登陆成功后，最后完善为跳转，走 get index 路线。这样 index 页面就会传入动态的数据。

```python
class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            #...
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
```























