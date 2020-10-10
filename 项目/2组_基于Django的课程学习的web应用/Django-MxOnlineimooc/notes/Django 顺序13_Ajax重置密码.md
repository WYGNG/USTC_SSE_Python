# Django 顺序13_Ajax重置密码

目的：在用户中心（登录状态）通过 Ajax 重置密码。



## 业务逻辑

逻辑类似于未登录时修改密码（users/views.ModifyPwdView）。

本次复用了 ModifyPwdView 用于表单验证的 ModelForm （ModifyForm）。

```python
class UpdatePwdView(View):
    """
    个人中心修改用户密码
    """
    def post(self, request):
        modify_form = ModifyForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            if pwd1 != pwd2:
                return HttpResponse('{"status":"fail", "msg":"密码不一致"}', content_type='application/json')
            user = request.user
            user.password = make_password(pwd1)
            user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"填写错误"}', content_type='application/json')

```



但是这里可以完善，如果把 ModelForm 表单验证的错误能够用 Ajax 传回去，前端就可以把错误显示出来。这里要可以用 `json.dumps()` 把表单验证的错误信息（字典形式）传递回前端。

```python
import json

class UpdatePwdView(View):
    def post(self, request):
        modify_form = ModifyForm(request.POST)
        if modify_form.is_valid():
            #...
        else:
            return HttpResponse(json.dumps(modify_form.errors), content_type='application/json')
```



## html结构

* 需要确保 name 能够正确被 ModelForm 接收。
* 需要加 csrf_token。

```html
<form id="jsResetPwdForm" autocomplete="off">
  <div class="box">
    <span class="word2">新&nbsp;&nbsp;密&nbsp;&nbsp;码</span>
    <input type="password" id="pwd" name="password1" placeholder="6-20位非中文字符"/>
  </div>
  <div class="box">
    <span class="word2">确定密码</span>
    <input type="password" id="repwd" name="password2" placeholder="6-20位非中文字符"/>
  </div>
  <div class="error btns" id="jsResetPwdTips"></div>
  <div class="button">
    <input id="jsResetPwdBtn" type="button" value="提交"/>
  </div>
  {% csrf_token %}
</form>
```



## jQuery 发送 Ajax 提交表单

* 对提交修改密码确认键进行监听
* 首先，对表单进行 `.serialize()` 然后作为 data 发送
* 单独的 JavaScript 文件不能使用模板语法，模板语法只能在 html 文件中使用。所以提交地址不能使用 `{% url 'update_pwd' %}` 。而是要使用网站 host 后面的相对路径，这里是 `/users/update/pwd/`。
* 在 Django 的表单验证中，错误的字段会放在 errors 中的键。假设字段名是 password1 的input 有误， `errors.password1` 就会出现。这时候传到前端，就是 `data.password1`。

```javascript
$('#jsResetPwdBtn').click(function(){
  $.ajax({
    cache: false,
    type: "POST",
    dataType:'json',
    url:"/users/update/pwd/",
    data:$('#jsResetPwdForm').serialize(),
    async: true,
    success: function(data) {
      if(data.password1){
        Dml.fun.showValidateError($("#pwd"), data.password1);
      }else if(data.password2){
        Dml.fun.showValidateError($("#repwd"), data.password2);
      }else if(data.status == "success"){
        Dml.fun.showTipsDialog({
          title:'提交成功',
          h2:'修改密码成功，请重新登录!',
        });
        Dml.fun.winReload();
      }else if(data.msg){
        Dml.fun.showValidateError($("#pwd"), data.msg);
        Dml.fun.showValidateError($("#repwd"), data.msg);
      }
    }
  });
});
```



前端还有具体的提取 password1 中的信息的函数

```javascript
var Dml = {};
    Dml.fun = {
        showErrorTips: function($elem,tips){
            $elem.html(tips).show();
            //setTimeout(function(){$elem.hide()},3000);
            return false;
        },
        showDialog: function(dialogBox){
            $('#jsDialog').show();
            $('#dialogBg').show();
            $('.dialogbox').hide();
           centerDialog(dialogBox);
            if(arguments[1]) $(arguments[1]).hide();
            if(arguments[2]) $(arguments[2]).hide();
        },
        showTipsDialog: function(obj){
            //type :'' || failbox
            var $Box = $('#jsSuccessTips'),
                h1 = obj.title || '提示',
                h2 = obj.h2 || '您的操作成功！';
                p = obj.p || '';
                type = obj.type || '';
            $('#jsDialog').show();
            $('#dialogBg').show();
            $('.dialogbox').hide();
            $Box.find('h1').html(h1);
            $Box.find('h2').html(h2);
            $Box.find('p').html(p);
            if(type){
                $Box.addClass(type);
                centerDialog($Box);
            }else{
                $Box.removeClass('failbox');
                centerDialog($Box);
            }
        },
        showComfirmDialog: function(obj){
            var $Box = $('#jsComfirmDialig'),
                h1 = obj.h1 || '确认提交',
                h2 = obj.h2 || '您确认提交吗？',
                callBack = obj.callBack;
            $('#jsDialog').show();
            $('#dialogBg').show();
            $('.dialogbox').hide();
            $Box.find('h1').html(h1);
            $Box.find('h2').html(h2);
            $('#jsComfirmBtn').on('click', function(){
                callBack();
            });
            centerDialog($Box);
        },
        showValidateError: function($elem,tips){
            var $tips = arguments[2] || '';
            $elem.focus();
            setTimeout(function(){
                $elem.parent().addClass('errorput');
                if($tips){
                    $tips.html(tips).show();
                }else{
                    if($elem.attr('id') == 'mobile-register-captcha_1'){
                        $('#jsMobileTips').html(tips).show();
                    }else if($elem.attr('id') == 'jsPhoneRegCaptcha'){
                        $elem.parent().siblings('.error').html(tips).show();
                    }else{
                        $elem.parent().siblings('.error').html(tips).show();
                    }
                }
            },10);
            return false;
        },
        getDate: function(){
            if (arguments[0]){
                var now = new Date(arguments[0])
            }else{
                var now = new Date();
            }

            return now.getFullYear() + '-' + (now.getMonth()+1) + '-' + now.getDate();
        },
        winReload: function(){
            var URL = arguments[0] || window.location.href;
            setTimeout(function(){
                window.location.href = URL;
            },1500);
        }
    };
    Dml.regExp = {
        phone: /^1([38]\d|4[57]|5[0-35-9]|7[06-8]|8[89])\d{8}$/,
        tel:/(^1([38]\d|4[57]|5[0-35-9]|7[06-8]|8[89])\d{8}$)|(^((\d{7,8})|(\d{4}|\d{3})-(\d{7,8})|(\d{4}|\d{3})-(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})|(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1}))$)/,
        email: /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/,
        phMail: /(^1([38]\d|4[57]|5[0-35-9]|7[06-8]|8[89])\d{8}$)|(^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+)/,
        number: /^[0-9]*$/,
        float: /^\d+(\.\d+)?$/,
        zsNumber: /^(-?[1-9]\d*|0)$/,
        name: /^[\u4e00-\u9fa5a-zA-Z]+$/,
        pwd: /^([^\u4e00-\u9fa5]{6,20})$/,
        verifyCode: /^[a-zA-z]{5}$/,
        phoneCode: /^\d{6}$/,
        emailCode: /^\d{4}$/,
        rsiName: /^[\u4e00-\u9fa5\-a-zA-Z0-9]{2,30}$/,
        //rsiName: /^([\u4e00-\u9fa5])([\u4e00-\u9fa5a-zA-Z0-9]+)$/,
        idCard: /(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/
    };
    Dml.Msg = {
        epUserName: '请输入登录手机或邮箱！',
        erUserName: '请输入正确的登录手机或邮箱！',
        epPhone: '请输入您的手机号码！',
        erPhone: '请输入正确的手机号码！',
        epTel: '请输入您的电话号码！',
        erTel: '请输入正确的电话号码，固定电话：区号-号码！',
        epVerifyCode: '请输入验证码！',
        erVerifyCode: '请输入正确的验证码！',
        epMail: '请输入您的邮箱！',
        erMail: '请输入正确的邮箱！',
        epPwd: '请输入登录密码！',
        erPwd: '密码为6-20位非中文字符！',
        epResetPwd: '请输入密码！',
        erResetPwd: '密码为6-20位非中文字符！',
        epRePwd:'请重复输入密码！',
        erRePwd:'两次密码输入不一致！',
        epPhCode: '请输入手机验证码！',
        erPhCode: '请输入正确的手机验证码！',
        epEmCode: '请输入邮箱验证码！',
        erEmCode: '请输入正确的邮箱验证码！',
        epName: '请输入您的姓名！',
        epNickName: '请输入昵称！',
    };
```





















