# Django 顺序14_全局消息数量显示

## 顺序

* request.user 在模板中是全局存在的
* 在 request.user 定义获取未读消息数量的方法
* 模板中调用获取数量的方法



## Model 中设置方法

在 users/models.py 中 UserProfile 中定义获取未读消息数量的方法

首先，在方法中引入 `operation.models` ，如果在开头就引入会形成循环引用。

然后，把用户 id 传入 UserMessage 中（因为 UserMessage 不是用外键，而是用 id ），返回 `count()` 数量即可。

```python
class UserProfile(AbstractUser):
    #...
    def unread_nums(self):
        # 获取用户未读消息数量
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id).count()
```



## html 中显示数量

直接调用`{{ request.user.unread_nums }}`

```html
<div class="msg-num">
  <span id="MsgNum">{{ request.user.unread_nums }}</span>
</div>
```



## 消息已读设置

### 1、未读消息记录的清空

在“我的消息”逻辑中，把所有的未读消息提取出来。用户进入消息中心就清空所有未读消息的记录。

apps/users/urls.py 

```python
class MymessageView(LoginRequiredMixin, View):
    """
    我的消息
    """
    def get(self, request):
        all_message = UserMessage.objects.filter(user=request.user.id)
        all_unread_messages = UserMessage.objects.filter(user=request.user.id, has_read=False)

        # 用户进入个人消息后，清空未读消息的记录
        for unread_message in all_unread_messages:
            unread_message.has_read = True
            unread_message.save()

```



### 2、未读消息数量的提取

在过滤条件中增加 `has_read=False`。

```python
class UserProfile(AbstractUser):
    #...
    def unread_nums(self):
        # 获取用户未读消息数量
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()
```



















