# Django 顺序9_显示choices值、外键反向获 model



## 显示字段的 choices 值

在模板中使用 `{{ course.get_degree_display }}` ，可以把 course 中的 degree 的 choices 的值显示出来。

```html
<span class="fl">难度：<i class="key">{{ course.get_degree_display }}</i></span>
```



## model 中定义新方法，外键反向获取 model

如果一个 model 有外键指向他，就可以用 `<使用外键的model>_set` 来反向获取使用了外键的 model。另外，获取到了 model 以后，可以定义新的方法，把业务处理的内容返回出去。

### 示例1：统计章节数

courses.models.py 中的 Course 并不带章节。但是章节外键指向 Course，因此可以反向去取章节。

```python
class Course(models.Model):
    #...
    def get_lesson_nums(self):
        all_lessons = self.lesson_set.all()
        return all_lessons.count()
```

在逻辑把 course 传递到模板以后，可以直接在模板中调用 `get_lesson_nums` 方法。

```html
<li><span class="pram word3">章&nbsp;节&nbsp;数：</span><span>{{ course.get_lesson_nums }}</span></li>
```

### 示例2：获取学习该课程的用户

同样在 courses.models.py 中定义新方法。切片只取5个。

```python
class Course(models.Model):
    #...
    def get_learn_users(self):
        return self.usercourse_set.all()[:5]
```

模板中的调用，首先得到的是 UserCourse，然后再用外键 user 去获取用户的头像。

```html
{% for user_course in course.get_learn_users %}
<span class="pic">
  <img width="40" height="40" src="{{ MEDIA_URL }}{{ user_course.user.image }}"/>
</span>
{% endfor %}
```











