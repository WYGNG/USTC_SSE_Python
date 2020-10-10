# Django 顺序17_收藏数

收藏数使用收藏接口 AddFavView 。



### 取消收藏

```python
class AddFavView(View):
    """
    用户收藏/用户取消收藏
    """
    def post(self, request):
        #...
        if exist_records:
            # 课程
            if int(fav_type) == 1:
                course = Course.objects.get(id=int(fav_id))
                course.fav_nums -= 1
                if course.fav_nums < 0:
                    course.fav_nums = 0
                course.save()

            # 课程机构
            elif int(fav_type) == 2:
                course_org = CourseOrg.objects.get(id=int(fav_id))
                course_org.fav_nums -= 1
                if course_org.fav_nums < 0:
                    course_org.fav_nums = 0
                course_org.save()

            # 讲师
            elif int(fav_type) == 3:
                teacher = Teacher.objects.get(id=int(fav_id))
                teacher.fav_nums -= 1
                if teacher.fav_nums < 0:
                    teacher.fav_nums = 0
                teacher.save()
```



### 增加收藏

增加收藏的操作。但是收藏数不能小于0，要做一个判断。

```python
class AddFavView(View):
    """
    用户收藏/用户取消收藏
    """
    def post(self, request):
        #...
        if exist_records:
            #...
        else:
            user_fav = UserFavorite()
            # 首先判断 fav_id 是否为 0，来判断是否取到该数值
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()

                # 课程
                if int(fav_type) == 1:
                    course = Course.objects.get(id=int(fav_id))
                    course.fav_nums += 1
                    course.save()

                # 课程机构
                elif int(fav_type) == 2:
                    course_org = CourseOrg.objects.get(id=int(fav_id))
                    course_org.fav_nums += 1
                    course_org.save()

                # 讲师
                elif int(fav_type) == 3:
                    teacher = Teacher.objects.get(id=int(fav_id))
                    teacher.fav_nums += 1
                    teacher.save()
```











