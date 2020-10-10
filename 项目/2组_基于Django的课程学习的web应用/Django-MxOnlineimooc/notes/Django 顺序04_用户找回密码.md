# Django 顺序4：用户找回密码



## 整体顺序

* 用户填写邮箱和验证码
* 服务器发送找回密码链接给用户邮箱
* 用户点击找回密码拦截进入重置密码页面
* 重置密码后，跳转到登录页面



## 脚手架

url

```python
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
```

users.views

```python
# 找回密码逻辑
class ForgetPwdView(View):
    def get(self, request):
        return render(request, "forgetpwd.html", {})
```

修改 login.html 中找回密码的跳转链接。

另外，在 forgetpwd.html 中修改静态文件的引用。



### forget_form

users.forms.py

```python
# 找回密码
class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})
```



users.views.py

这样才有验证码

```python
from .forms import ForgetForm
# 找回密码逻辑
class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form":forget_form})
```



























