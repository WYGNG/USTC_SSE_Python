# Django 顺序6_ModelForm以及Ajax提交表单



表单验证中设定的检验条件，有时和后面要存入的 model 非常类似，因此 Django 有方法把 model 转化成 form 用以表单验证，这种 form 名叫 ModelForm。



### 普通表单

```python
from django import forms

class UserAskForm(forms.Form):
    name = forms.CharField(required=True, min_length=2, max_length=20)
    phone = forms.CharField(required=True, min_length=11, max_length=11)
    course_name = forms.CharField(required=True, min_length=5, max_length=50)
```



经过对照 model（operation.UserAsk），发现字段的条件几乎相同。

唯一就是 form 中的 `require=True` 可以理解成 `null=False`。实际上字段也是默认不为空。

```python
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    course_name = models.CharField(max_length=50, verbose_name='课程名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
```

所以 model 可以直接转化成 ModelForm 用。



### ModelForm

ModelForm 写成以下形式。其中 `model=UserAsk` 表示继承自 `UserAsk` 表，并且可以选择其中的字段，也可以像普通 form 一样，自己可以新增加字段。

```python
from operation.models import UserAsk

class AskUserForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
```



## urls：机构类的路由放在 organization 的 app 下 

首先在主 urls 下

```python
urlpatterns = [
    # 课程机构 url 配置
    url(r'^org/', include('organization.urls', namespace="org")),
]
```

在机构下面的 urls 中

```python
from .views import OrgView
urlpatterns = [
    # 课程机构列表页
    url(r'list/$', OrgView.as_view(), name="org_list"),
]
```



### ModelForm 逻辑

本逻辑目的是处理用户的咨询表单提交（AJAX 形式），如果合格则保存，否则返回失败状态和错误信息。

因为是处理 AJAX，所以返回的的内容有三个重点：

* 以 HttpResponse() 返回
* 返回的是字典格式的字符串
* HttpResponse() 的第二个参数是 `content_type='application/json'` 。

```python
from .forms import UserAskForm
class AddUserAskView(View):
    """
    用户咨询
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            # ModelForm 可以直接保存进数据库，一定要带参数 commit=True
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}', content_type='application/json')
```



### urls：用户咨询的路由

把刚才的业务逻辑配置到 url 中。

```python
from .views import AddUserAskView

urlpatterns = [
    # 用户询问课程
    url(r'add_ask/$', AddUserAskView.as_view(), name="add_ask")
]
```



### 用户端的 ajax 请求

用户咨询表单用 ajax 与服务端交互。逻辑如下：

* 监听 `#jsStayBtn` 这个按钮的 `click` 事件
* 发生该事件，向 url 发送 POST 请求，该 url 的值可以用 Django 的模板
* 把表单 `#jsStayForm` 进行序列化 `.serialize()` ，注意表单中要加上 `{% csrf_token %}`
* 返回成功之后，就 alert 提交成功。如果状态是 `fail` 就把错误提示显示html中。

```javascript
<script>
  $(function () {
    $('#jsStayBtn').on('click', function () {
      $.ajax({
        cache: false,
        type: "POST",
        dataType: "json",
        url: "{% url 'org:add_ask' %}",
        //表单提交可以用 serialize 方法把 csrf token 一块序列化过来
        data: $('#jsStayForm').serialize(),
        async: true,
        success: function (data) {
          if (data.status == 'success') {
            $('#jsStayForm')[0].reset();
            alert("提交成功")
          } else if (data.status == 'fail') {
            $('#jsCompanyTips').html(data.msg)
          }
        },
        error: function(error) {
          console.log('error')
          // console.log(error.responseText.msg)
        }
      });
    });
  })
</script>
```



### 完善表单验证：正则检验手机号码

organization.forms.py

* 函数名称一定要 `clean_字段名`
* 从自身检验过的数据中取出来，再匹配新的规则
* 合格返回任意值
* 不合格，`raise forms.ValidationError("显示的信息", code="WhatYouLike")`

```python
# 用户提交咨询表单的验证
class UserAskForm(forms.ModelForm):
    #...

    def clean_mobile(self):
        """
        验证手机是否合法
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码不合法",code="InvalidateMobile")
```









