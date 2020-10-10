# Django 顺序11_全局搜索功能



搜索主要通过 url 拼串完成。

```python
url?keywords=[搜索关键词]
```



## 业务逻辑部分

比如搜索课程中，提取：标题或者描述中包含搜索关键词的记录，并返回模板。

organization/views.py

```python
from django.db.models import Q

class CourseListView(View):
    def get(self, request):
        # 关键词搜索功能
        search_keywords = request.GET.get("keywords", "")
        if search_keywords:
            # 搜索课程名，Q()|Q() 表示并列
            all_courses = all_courses.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords))
        #...
```



## 前端发送请求

html 内容

```html
<div class="selectContainer fl">
  <span class="selectOption" id="jsSelectOption" data-value="course">
    公开课
  </span>
  <ul class="selectMenu" id="jsSelectMenu">
    <li data-value="course">公开课</li>
    <li data-value="org">课程机构</li>
    <li data-value="teacher">授课老师</li>
  </ul>
</div>
```





static/js/deco-common.js

* 获得搜索关键词 `keywords = $('#search_keywords').val()` 
* 获取类型，类型放在 `data-value` 属性中
* 分别对类型与关键词拼串，并跳转到相应的页面 `window.location.href=` 

```javascript
//顶部搜索栏搜索方法
function search_click(){
    var type = $('#jsSelectOption').attr('data-value'),
        keywords = $('#search_keywords').val(),
        request_url = '';
    if(keywords == ""){
        return
    }
    if(type == "course"){
        request_url = "/course/list?keywords="+keywords
    }else if(type == "teacher"){
        request_url = "/org/teacher/list?keywords="+keywords
    }else if(type == "org"){
        request_url = "/org/list?keywords="+keywords
    }
    window.location.href = request_url
}

// 触发搜索事件
$('#jsSearchBtn').on('click',function(){
        search_click()
    });
```



























