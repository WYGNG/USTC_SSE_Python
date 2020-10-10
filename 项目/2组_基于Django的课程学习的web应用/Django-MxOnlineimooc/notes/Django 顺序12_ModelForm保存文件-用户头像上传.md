# Django 顺序12_ModelForm保存文件-用户头像上传





## 配置 /users/urls.py

```python
from .views import UploadImageView

urlpatterns = [
    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
]
```



## 配置 ModelForm

为了使用 Django 的 form 来直接保存到数据库。

```python
from .models import UserProfile

# 处理文件的上传
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
        pass
```



## 逻辑

首先，实例化 form，但是传入参数的时候，除了 `request.POST` 还要传入 `request.FILES`。

因为文件都是单独存放在 requst 的 FILES 中，而不是 POST 字典内。

一旦通过参数把文件引入 form，文件就保存在了 form 中。

```python
from .froms import UploadImageForm

class UploadImageView(LoginRequiredMixin, View):
    """
    用户修改头像
    """
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES)
        pass
        
```

断点打在 `image_form…` 上面准备调试。



## HTML 内容

首先，在 form 的属性中，必须指明 `enctype="multipart/form-data"`，才能把文件传递到后台。另外要带上 `{% csrf_token %}`。

最后要确认 `<input type="file" name="image" id="avatarUp" class="js-img-up"/>`中的 name属性与逻辑中实例化的 form 中的 name 一样。 

```python
<form class="clearfix" id="jsAvatarForm" enctype="multipart/form-data" autocomplete="off" method="post" action="{% url 'users:image_upload' %}" target='frameFile'>
  <label class="changearea" for="avatarUp">
    <span id="avatardiv" class="pic">
      <img width="100" height="100" class="js-img-show" id="avatarShow"
      src="{{ MEDIA_URL }}{{ request.user.image }}"/>
    </span>
    <span class="fl upload-inp-box" style="margin-left:70px;">
    <span class="button btn-green btn-w100" id="jsAvatarBtn">修改头像</span>
      <input type="file" name="image" id="avatarUp" class="js-img-up"/>
    </span>
  </label>
  {% csrf_token %}
</form>
```



## 保存图片文件

### 方法1：取出 form 验证过的 image 保存

上传文件在断点处可以看见 request.FILES 中显示 `'image'={InMemoryUploadedFile}`。

再查看 Django 的 form 中是否保存，步进调试到 `pass` 位置，然后查看到

`image_form.cleaned_data.'image'` 中也是 `{InMemoryUploadedFile}`。

* image 验证通过了。
* 可以用字典取该值，并保存在用户数据库中

```python
class UploadImageView(LoginRequiredMixin, View):
    """
    用户修改头像
    """
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.cleaned_data['image']
            request.user.image = image
            request.user.save()
            pass
```



### 方法2：用 ModelForm 的 instance 参数传入

可以直接对 ModelForm 保存

```python
class UploadImageView(LoginRequiredMixin, View):
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            pass
```

















