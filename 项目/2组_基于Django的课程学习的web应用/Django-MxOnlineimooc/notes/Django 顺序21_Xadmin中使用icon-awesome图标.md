# Django 顺序21_Xadmin使用icon-awesome图标

Xadmin使用4.0.3，官网下载icon-awesome 4.7版本。

```python
http://fontawesome.io/
```

解压并拷贝其中`fonts` 与 `css` 目录，并拷贝到 xadmin/static/xadmin/vendor/font-awesome 目录中替换原来的文件夹。



使用就是在 adminx.py 中，每个 class 中使用 `model_icon`，填写的值参照 icon-awesome 官网，fa必须有，后面 `fa-xxx` 是图标名称。比如

```python
class EmailVerifyRecordAdmin():
    model_icon = 'fa fa-address-book-o'
```













