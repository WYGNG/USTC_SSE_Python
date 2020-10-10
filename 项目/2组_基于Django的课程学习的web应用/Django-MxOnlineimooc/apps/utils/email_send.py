# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/7/17 11:30 AM'

from users.models import EmailVerifyRecord
from uuid import uuid4
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str()[:4]
    else:
        code = random_str()

    # 用户注册邮件中的信息，赋值到 model 实例中
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    # 发送的邮件内容逻辑
    email_title = ""
    email_body = ""

    # 注册类邮件内容
    if send_type == "register":
        email_title = "慕学在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "慕学在线网密码重置链接："
        email_body = "请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "慕学在线邮箱修改验证码："
        email_body = "你的邮箱验证码为：{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

def random_str():
    # 用 uuid.uuid4() 生成 36 位的随机uuid，再用 str() 转化成字符串，只取前 16 位
    return str(uuid4())[:16]
