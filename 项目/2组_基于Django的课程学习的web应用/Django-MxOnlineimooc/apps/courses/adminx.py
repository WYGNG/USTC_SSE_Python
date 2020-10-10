# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/6/17 11:13 AM'


import xadmin
from .models import Course, Lesson, Video, CourseResource
from organization.models import CourseOrg


# class LessonInline(object):
#     module = Lesson
#     extra = 0

# 添加model
class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums', 'add_time', 'get_lesson_nums', 'go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['fav_nums']
    list_editable = ['degree', 'desc']
    exclude = ['click_nums']
    refresh_times = [3, 5]
    # inlines = [LessonInline]

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()


# 添加model
class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # course 是一个对象，xadmin 不能搜索，需要指定搜索 course 对象里哪一个属性
    list_filter = ['course__name', 'name', 'add_time']

# 添加model
class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']

# 添加model
class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'add_time']

# 添加model
class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['fav_nums']
    exclude = ['click_nums']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

# xadmin.site.register(BannerCourseAdmin, BannerCourse)

