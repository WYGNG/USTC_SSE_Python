# Django 顺序22_Xadmin的布局



## 倒叙排列 ordering

adminx.py 中 ordering，比如

```python
class CourseAdmin():
    #...
    ordering = ['-click_nums']
```



## 只读字段 readonly_fields  

admin.py 中

```python
class CourseAdmin():
    #...
    readonly_fields = ['click_nums', 'fav_nums']
```



## 不显示字段 exclude

注意：与readonly冲突，不要同时设置

```python
class CourseAdmin():
    readonly_fields = ['fav_nums']
    exclude = ['click_nums']
```



## 字段设置为搜索 relfield_style

organization/adminx.py

```python
class CourseOrgAdmin(object):
    #...
    relfield_style = 'fk-ajax'
```



## 外键表添加，关键他的表也同时添加 inline

```python
class LessonInline(object):
    module = Lesson
    extra = 0

class CourseAdmin():
    inlines = [LessonInline]
```



## 两个显示器共用一张表（不同逻辑） proxy

一定要设置 `proxy=True`，才能达到共用一张表的目的，否则会产生两张表。

crosses/models.py

```python
class BannerCourse(Course):
    """
    专门显示 banner course
    """
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        proxy = True
```



只显示 is_banner=True 的数据

```python
class BannerCourseAdmin(object):
    # 与 CourseAdmin 相同
    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs
```



## 列表栏可以直接编辑 list_editable

```python
class CourseAdmin(object):
    #...
    list_editable = ['degree', 'desc']
```



## 列表栏显示函数的返回值 

courses/models.py 中定义了函数获得章节数

```python
class Course(models.Model):
    #...
    def get_lesson_nums(self):
        """
        获取课程章节数
        """
        all_lessons = self.lesson_set.all()
        return all_lessons.count()

    get_lesson_nums.short_description = "章节数"
```



这个 `get_lesson_nums` 函数可以直接传递到 adminx.py 中显示。

```python
class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums', 'add_time', 'get_lesson_nums']
```



另外可以设置列表栏中跳转

```python
class Course(models.Model):
    #...

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.projectsedu.com'>跳转</a>")

    go_to.short_description = "章节数"
```

```python
class CourseAdmin(object):
    list_display = [#..., 
        'get_lesson_nums']
```





## 定时刷新功能 refresh_times

在 xadmin.py 中有一个 refresh.py

```python
class RefreshPlugin(BaseAdminPlugin):
    refresh_times = []
```



```python
class CourseAdmin(object):
    #...
    refresh_times = [3, 5]
```



## 保存之前实现功能

```python

class CourseAdmin(object):
    #...

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()
```





















