# Django 顺序16_学习人数与点击数

本章主要是逻辑方面的内容。



## 点击数

### 1. 课程详情页

```python
class CourseDetailView(View):
    """
    课程详情页
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 增加课程点击数
        course.click_nums += 1
        course.save()
```



### 2. 讲师详情页

```python
class TeacherDetailView(View):
    def get(self, request, teacher_id):

        teacher = Teacher.objects.get(id=int(teacher_id))
        teacher.click_nums += 1
        teacher.save()
```



### 3. 课程机构首页

```python
class OrgHomeView(View):
    """
    机构首页
    """

    def get(self, request, org_id):
        # 为了让页面知道当前是哪个分页
        current_page = "home"

        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()
```







## 学习人数

### 1. 课程章节信息（点击了“开始学习”）

```python
class CourseInfoView(LoginRequiredMixin, View):
    """
    课程章节信息
    """

    def get(self, request, course_id):
        # 获取 url 参数确定课程
        course = Course.objects.get(id=int(course_id))
        course.students += 1
        course.save()
```







