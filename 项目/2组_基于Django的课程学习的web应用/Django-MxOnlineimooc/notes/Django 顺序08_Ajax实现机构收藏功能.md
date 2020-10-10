# Django 顺序8_Ajax实现机构收藏功能



## 后端逻辑部分

逻辑处理顺序：

* 判断用户是否登录



### 判断用户是否登录

django 的 request，即使用户没登录的情况，也有一个 user。该 user 是一个匿名的用户。而且也可以对 user 进行判断是否登录。

在全局查找用过的函数，可以用 `find in path`，在 Mac 默认的 keymap 是`command + shift + F` 。

因此对于用户是否登录的判断方法是`.is_authenticated()`。

```python
        if request.user.is_authenticated()
```

对于没有登录的用户，发送 json 告诉 Ajax 用户未登录。而是否跳转到登录页面，由 Ajax 控制，这里主要负责返回 Json 数据。

```python
class AddFavView(View):
    def post(self, request):
        # 查询是否存在
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')
```



### 判断用户收藏状态

顺序：

* 用户就是 `request.user`
* 收藏的 id，以及收藏的类型（机构还是讲师等）要一起联合查询
* 如果数据库中存在收藏记录，可认为用户要“取消收藏”。把数据记录从数据库中删除。
* 如果不存在，则向数据库中保存记录。



注意点：

* 返回都是符合 Ajax 交互规则的 `return HttpResponse('{"status":"success"}', 'application/json')`
* 对于从 Ajax 获取到的数据，比如 fav_id 和 fav_type，要进行整型转换 `int()`。
* 因为要 int 转换，所以从 Ajax 用 `.POST.get` 获取数据时，要设置一个值，比如 0。不能为空字符串，否则后面用 `int()` 抛异常。
  ​

完整逻辑代码

```python
class AddFavView(View):
    """
    用户收藏/用户取消收藏
    """
    def post(self, request):
        # 接收 Ajax 传递的参数
        # fav_id 与 fav_type 没取到，则用 0 为默认值，为了防止 int(fav_id) 抛异常。
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        # 判断用户登录状态
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')


        # 查询是否存在收藏记录
        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            # 如果记录已经存在，则表示用户取消收藏
            exist_records.delete()
            return HttpResponse('{"status":"success","msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            # 首先判断 fav_id 是否为 0，来判断是否取到该数值
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status":"success","msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail","msg":"收藏出错"}', content_type='application/json')

```



### 增加 urls

用以接收 Ajax 请求（用户收藏事件）。

```python
from .views import AddFavView

urlpatterns = [
    #...
    url(r'add_fav/$', AddFavView.as_view(), name="add_fav"),
]
```



## 前端：发起请求处理

在公用页 org_base.html 中

html 的按钮

```html
<div class="btn fr collectionbtn  notlogin" data-favid="22" data-fav-type="1">收藏</div>
```

css 部分

```css
.btn {
    display: inline-block;
    margin-bottom: 0;
    font-weight: 200;
    text-align: center;
    vertical-align: middle;
    touch-action: manipulation;
    cursor: pointer;
    text-decoration: none;
    box-sizing: content-box;
    background-image: none;
    border: 1px solid transparent;
    -webkit-appearance: none;
    white-space: nowrap;
    outline: none;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}
.btn:hover,
.btn:focus,
.btn.focus {
    color: #fff;
    text-decoration: none;
}
.btn:active,
.btn.active {
    outline: 0;
    background-image: none;
}
```



### jQuery 捕捉按钮点击事件，并调用 Ajax 请求函数 add_fav

向 Ajax 请求函数中传入了三个参数：

* 第1个参数：`$(this)`是按钮这个元素。
* 第2个参数：`{{ course_org.id }}` 是 fav_id，也就是课程机构的id。
* 第3个参数：`2` 是 fav_type，收藏类型是2，这是在 UserFavorite 这个 model 设定的。2 表示课程机构。

```javascript
$('.collectionbtn').on('click', function () {
    add_fav($(this), {{ course_org.id }}, 2);
});
```



### Ajax 发送请求的函数 add_fav

#### csrf_token 在非表单 post 中的设置

csrf_token 最关键的地方：在 xhr 这个对象的头部中设置 csrf_token 参数。因为这里 post 请求的并不是一个 form，所以没有办法在 form 里面加入 `{% csrf_token% }`，所以直接在 Ajax xhr对象的头部中设置 `{{ csrf_token }}` 的值。这是 jQuery 的用法。

```javascript
function add_fav(current_elem, fav_id, fav_type){
  $.ajax({
    //...
    beforeSend: function(xhr, settings){
      xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}")
    },
    //...
  })
}
```

#### add_fav 处理回调数据（服务端传回）的逻辑

* 如果状态是 fail
  * 如果 `data.msg` 是“用户未登录”，则跳转到登录页面
  * 如果是其他内容，则把 `data.msg` 在浏览器中 alert 出来。
* 如果状态是success，把 `data.msg` 的内容写入 `data.msg`。

```javascript
function add_fav(current_elem, fav_id, fav_type) {
  $.ajax({
    cache: false,
    type: "POST",
    url: "{% url 'org:add_fav' %}",
    data: {'fav_id': fav_id, 'fav_type': fav_type},
    async: true,
    beforeSend: function (xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
    },
    success: function (data) {
      if (data.status == 'fail') {
        if (data.msg == '用户未登录') {
          window.location.href = "{% url 'login' %}";
        } else {
          alert(data.msg)
        }  
      } else if (data.status == 'success') {
        current_elem.text(data.msg)
      }
    },
  });
}

$('.collectionbtn').on('click', function () {
  add_fav($(this), {{ course_org.id }}, 2);
});
```



## 完善模板 html 显示

在每个机构的分页中相互跳转时，即使该机构已经收藏，也不能正确显示出来，因此每个分页都需要对收藏状态进行判断。

首先，业务逻辑要判断用户是否登录、是否收藏，并通过业务逻辑把收藏状态参数传递到 html 中。以一个分页的逻辑举例。

```python
class OrgHomeView(View):
    def get(self, request, org_id):
        #...
        # 判断是否收藏该机构。默认未收藏
        has_fav = False
        # fav_id 就是机构的 id，因为 Ajax 提交的是机构 id
        # 因为明确是机构，fav_type = 2
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        return render(request, 'org-detail-homepage.html', {
            #...
            'has_fav': has_fav
        })
```



在 org_base.html 中进行判断

```html
<div class="btn fr collectionbtn  notlogin" data-favid="22" data-fav-type="1">{% if has_fav %}已收藏{% else %}收藏{% endif %}</div>
```









