# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from .models import Course, CourseResource, Video
from operation.models import UserFavorite, CourseComments, UserCourse
from utils.mixin_utils import LoginRequiredMixin


class CourseListView(View):
    """
    课程列表页
    """

    def get(self, request):

        all_courses = Course.objects.all().order_by("-add_time")

        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        # 关键词课程搜索功能
        search_keywords = request.GET.get("keywords", "")
        if search_keywords:
            # 搜索课程名
            all_courses = all_courses.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords)|
                                             Q(detail__icontains=search_keywords))

        # 排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_courses = all_courses.order_by("-students")
        elif sort == 'hot':
            all_courses = all_courses.order_by("-click_nums")

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 3, request=request)

        courses = p.page(page)

        org_nums = all_courses.count()

        return render(request, "course-list.html", {
            'all_courses': courses,
            "sort": sort,
            'hot_courses': hot_courses,
        })


class CourseDetailView(View):
    """
    课程详情页
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 增加课程点击数
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated():
            # 判断用户是否收藏课程，课程 fav_type=1
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            # 模板中用 for 循环，所以要传入数组，即使是空数组
            relate_courses = []

        return render(request, "course-detail.html", {
            'course': course,
            'relate_courses': relate_courses,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org,
        })


class CourseInfoView(LoginRequiredMixin, View):
    """
    课程章节信息
    """

    def get(self, request, course_id):
        # 获取 url 参数确定课程
        course = Course.objects.get(id=int(course_id))
        course.students += 1
        course.save()

        # 查询用户是否已经关联了该课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        # 如果没有关联，则关联
        if not user_courses:
            user_courses = UserCourse(user=request.user, course=course)
            user_courses.save()

        """
        解决问题：学过这门课程的用户，还学过其他什么课程
        UserCourse 根据课程的 id 筛选出所有的记录。
        通过这个记录可以得到所有学过这门的 user
        获得了所有学过这门课的 user 的 id
        """
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]

        """
        要了解学过这门课的学生，还学过什么课程
        还是回到 UserCourse 表，用刚才获得的用户 id 去获取所有的课程
        user_id （user 外键，取 id 用 user_id
        user_id__in （双下划线）表示去查找数组中的内容
        """
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)

        # 取出所有课程 id
        course_ids = [user_course.course.id for user_course in all_user_courses]

        # 查询学过这门的课用户们，总共学过些课
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]

        course_resources = CourseResource.objects.filter(course=course)

        return render(request, "course-video.html", {
            'course': course,
            'course_resources': course_resources,
            'relate_courses': relate_courses,
        })


class ComentsView(LoginRequiredMixin, View):
    """
    显示课程评论
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.all()

        return render(request, "course-comment.html", {
            'course': course,
            'course_resources': course_resources,
            'all_comments': all_comments
        })


class AddCommentsView(View):
    """
    用户添加课程评论
    """
    def post(self, request):
        # 判断用户是否登录
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', 'application/json')

        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments", "")

        if int(course_id)>0 and comments:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.user = request.user
            course_comments.comments = comments
            course_comments.save()
            return HttpResponse('{"status":"success","msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加失败"}', 'application/json')


class VideoPlayView(View):
    """
    课程视频播放：
    一部分与 CourseInfoView 类一样
    """

    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        course = video.lesson.course

        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_courses = UserCourse(user=request.user, course=course)
            user_courses.save()

        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]

        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)

        course_ids = [user_course.course.id for user_course in all_user_courses]

        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]

        course_resources = CourseResource.objects.filter(course=course)

        return render(request, "course-play.html", {
            'video': video,
            'course': course,
            'course_resources': course_resources,
            'relate_courses': relate_courses,
        })































