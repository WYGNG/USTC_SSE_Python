# Django 顺序5_设置media显示图片



## settings 设置

Django 通过后台（admin或xadmin）上传图片之前，需要设置 media 路径与文件夹。

主要处理 `ImageField`字段，这里 upload_to 中，`%Y` 表示年，`%m` 表示月。

```python
class CourseOrg(models.Model):
    image = models.ImageField(default='', upload_to='org/%Y/%m', verbose_name='logo', max_length=100)
```



在项目目录下新建文件夹，名叫 `media`，并在 settings 中设置 media 路径与目录。

```python
import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```



## 模板中图片地址

如何把 ImageField 转化成图片地址？

首先，ImageField 存储方式就是字符串，是图片的相对路径地址。`{{ course_org.image }}` 是相对路径，还需要在前面加上 settings 中配置的 MEDIA_URL，可以写成

```python
<img width="200" height="120" class="scrollLoading" src="{{ MEDIA_URL }}{{ org.image }}"/>
```



## settings 中配置模板的处理器

在 TEMPLATES 中 OPTIONS 中的 context_processors 中需要加上`'django.template.context_processors.media'`。

这个从 Django 1.8 之前是 `'django.core.context_processors.media'`，现在从 core 更换为指导 template。

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                #...
                'django.template.context_processors.media',
            ],
        },
    },
]
```



到这一步，仍然不能显示图片，在网页源代码中可以看到有图片的地址。但是仍然需要在 urls 中配置图片地址的路由，让 Django 知道到那个地方去取回图片。



## urls 配置

需要引入一个方法处理静态文件

```python
from django.views.static import serve
```

另外需要从 settings 中引入设置好的 media 目录地址 MEDIA_ROOT

```python
from MxOnline.settings import MEDIA_ROOT
```

最后在 url 中配置完整如下

```python
# -*- coding:utf-8 -*-
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT

urlpatterns = [
    # 处理 media 信息，用于图片获取
    url(r'^media/(?P<path>.*)', serve, {"document_root":MEDIA_ROOT}),
]
```



至此就可以显示出来图片。









