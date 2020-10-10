# Django 顺序3：用户注册与激活



## 基础搭建

### 路由配置 urls.py

```python
from users.views import LoginView, RegisterView

urlpatterns = [
    # 用户注册
    url(r'^register/$', RegisterView.as_view(), name='register'),
]
```



### 逻辑业务 users.views.py

```python
# 用户登录
class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")
```



### 模板页面 templates.register.html

增加引用静态文件。

```html
{% load staticfiles %}
```





## 验证码包 django-simple-captcha==0.4.6

### 注册到 settings 

放入 INSTALLED_APPS

```python
INSTALLED_APPS = [
    #...
    'captcha',
]
```

配置路由 urls.py。

```python
from django.conf.urls import url, include
urlpatterns = [
    # 验证码图片的路由
    url(r'^captcha/', include('captcha.urls')),
]
```

makemigrations/migrate 之后，在数据库中出现表名叫“captcha_captchastore”。

注意路由中不能带`$`，因为是include，需要留给包含的其他路由地址用，还不能用`$`结束。

不能写成：

```python
    url(r'^captcha/$', include('captcha.urls')),
```





### 定义带验证码字段的 form

注意这里不是 `form.CaptchaField()`。

```python
from captcha.fields import CaptchaField
# 登录表单验证，加入了验证码
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()
```



### get 请求时，把 register_form 返回到模板中

注意这里 `RegisterForm()` 中不需要带参数，因为不做验证。

```python
from .forms import RegisterForm
# 用户登录
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})
```





### html 模板中引用 captcha 验证码

首先在 views 逻辑中实例化，再返回给模板。最后在模板中调用。就可以打开调试看到验证码出来。点击验证码区域会更换验证码。

```python
<div class="form-group marb8 captcha1 errorput">
    <label>验&nbsp;证&nbsp;码</label>
    {{ register_form.captcha }}
</div>
```

django-simple-captcha 包自己实现了 html 代码。其中包含一段属性为 hidden 的输入框，这是 captcha 生成的 hash key，name 是 `captcha_0`。而用户输入的是 input 的 name 是 `captcha_1`。最终这两个字段都会返回服务器，captcha 包在 captcha 表中进行对比核实。

```html
<div class="form-group marb8 captcha1 errorput">
    <label>验&nbsp;证&nbsp;码</label>
    <img src="/captcha/image/04599e1d3def39ef70b21cb48326d5882d919447/" alt="captcha" class="captcha" /> <input id="id_captcha_0" name="captcha_0" type="hidden" value="04599e1d3def39ef70b21cb48326d5882d919447" required /> <input autocomplete="off" id="id_captcha_1" name="captcha_1" type="text" required />
</div>
```



### post逻辑中，验证 captcha

需要把 request.POST 放入 form 实例化的参数中。

```python
# 用户登录
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            pass
```



### 自定义 form 表单错误文字（以中文显示）

captcha的表单错误是英文的内容，显示

```html
<li>Invalid CAPTCHA</li>
```

在 form 中自定义成中文内容，修改字段参数 errors_messages，该参数的值是一个字典，修改其中的 invalid。

```python
class RegisterForm(forms.Form):
    #...
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})
```



### 保存用户注册信息到数据库

逻辑顺序：

* 取出 post 表单中的数据
* 实例化一个 model （数据库的表）
* 把表单数据保存到实例化的 model 中（最后是`.save()`）

这里的注意点是，密码不能以明文保存进数据，需要先用 auth.hasers 中 `make_password` 方法将用户输入的密码加密以后，再保存进数据库。

另外，由于是邮箱注册，所以该注册用户的用户名与邮箱都是用户输入的邮箱。

```python
from django.contrib.auth.hashers import make_password

# 用户登录
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.save()
```



## 发送注册邮件

### 发送邮件逻辑

在 apps 目录下建立 utils package 目录（里面带 `__init__.py`），并在里面建立 email_send.py。

首先，需要把发送给用户的注册邮件信息保存在数据库，当用户点击邮件注册链接之后，需要在数据核实是否存在这些信息，存在才能激活用户。否则报错不存在该用户。

```python
from users.models import EmailVerifyRecord

def send_register_email(email, type=0):
    email_record = EmailVerifyRecord()
```



### 生成随机字符串

```python
# -*- coding:utf-8 -*-
from users.models import EmailVerifyRecord
from uuid import uuid4

def send_register_email(email, type=0):
    email_record = EmailVerifyRecord()
    code = random_str()

def random_str():
    # 用 uuid.uuid4() 生成 36 位的随机uuid，再用 str() 转化成字符串
    return str(uuid4())
```



### 保存发送给用户的邮件关键信息

放入实例化的 model 中，用于用户点击邮件链接激活时核实信息验证。激活码、邮箱名、发送类型。

```python
def send_register_email(email, send_type='register'):
    #...
    # 用户注册邮件中的信息，赋值到 model 实例中
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
```



### 激活邮件的内容编写

```python
def send_register_email(email, send_type='register'):
    #...
    # 发送的邮件内容逻辑
    email_title = ""
    email_body = ""

    # 注册类邮件内容
    if send_type == "register":
        email_title = "慕学在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)
```



### 发送邮件函数

在 settings 中设定发送邮件参数

```python
EMAIL_HOST = 'smtp.sina.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'timm_lee@sina.com'
EMAIL_HOST_PASSWORD = 'lkj;lkhkjg'
EMAIL_USE_TLS = True
EMAIL_FROM = 'timm_lee@sina.com'
```

Django 自带发送邮件函数 send_mail()

```python
from django.core.mail import send_mail

send_mail(subject, message, from_email, recipient_list,
              fail_silently=False, auth_user=None, auth_password=None,
              connection=None, html_message=None)
```

* subject 是主题
* message 是邮件内容，就是body
* from_email 是 settings 中设置的发件人 EMAIL_FROM
* recipient_list 必须是一个 list，是收人人的列表。

所以发送函数设置，邮件发送函数成功发送邮件以后会返回值。

```python
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
```



### users.views.py 引入发送邮件函数

这里的 user_name 接收用户的注册邮箱信息。成功去登录页面，失败则返回登录页面。

```python
from utils.email_send import send_register_email

class RegisterView(View):
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
        	#...
            send_register_email(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html")
```



### 注册表单验证向模板返回信息

错误信息的返回类似于用户注册部分。

而这里有个关键是如果客户输入错误，则还是把刚才的 email 填入新的注册表单中。使用了 `{{ register_form.email.value }}` 值。密码也是把值也填进去。

```html
<input type="text" id="id_email" name="email" value="{{ register_form.email.value }}">
```



## 用户激活

### 将注册用户设置为“未激活”

在保存注册用户的时候，先把客户是否激活设置为 False

```python
# 用户注册
class RegisterView(View):
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            #...
            user_profile.is_active = False
```



### 激活链接设置

关键点是提取 url 中的变量，url 中变量的设置是 

`(?P<变量名>变量的正则表达式)`

比如名为 active_code 的变量，正则是所有的字符（.*），可以写成

`(?P<active_code>.*)`

放在active链接下面就是：

```python
url(r'^active/(?P<active_code>.*)/$', ),
```



### 激活 view 接收激活码

首先要接收到激活链接中的参数 active_code

```python
# 用户激活链接逻辑
class ActiveUserView(View):
    def get(self, request, active_code):
        pass
```

完整 url 是

```python
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
```

当用户输入以下 url 地址的时候，可以在 views 中得到激活码。

```python
http://127.0.0.1:8000/active/142ed43a-1f3d-428c-94d2-599027bb3032/
```



### 激活逻辑

首先，根据激活码，从邮件验证 model 中筛选是否存在激活码的发送激活码记录。

如果存在发送激活码记录，则取出该记录。

然后，把发送激活码记录中 email 取出来。

再根据该 email 去用户注册信息中获取记录。

将用户的激活状态改为已激活，并保存。

```python
# 用户激活链接逻辑
class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        return render(request, "login.html")
```



### 完善用户登录逻辑（增加激活判断）

用户未激活则报错。

```python
class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            #...
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "用户未激活"})
```



### 完善注册逻辑（增加判断用户email是否已经注册）

```python
# 用户注册
class RegisterView(View):
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, "login.html", {"msg": "用户已经存在", "register_form": register_form})
```

如果注册过报错，而且把注册的 form 传回，一是保证有验证码，二是回填数据。



### 完善激活逻辑（增加用户不存在判断分支）

新建链接失效的页面：active_fail.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>链接失效</title>
</head>
<body>
<p>链接失效</p>
</body>
</html>
```

如果激活时，用户不存在则调整失效页面。

```python
# 用户激活链接逻辑
class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            #...
        else:
            return render(request, "active_fail.html")
```

















