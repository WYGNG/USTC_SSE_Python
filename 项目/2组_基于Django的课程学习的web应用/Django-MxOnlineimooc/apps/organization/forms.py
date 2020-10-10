# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/7/17 4:31 PM'

import re

from django import forms
from operation.models import UserAsk


# 用户提交咨询表单的验证
class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机是否合法
        """
        mobile = self.cleaned_data['mobile']

        return mobile
        # REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176{8}$"
        # p = re.compile(REGEX_MOBILE)
        # if p.match(mobile):
        #     return mobile
        # else:
        #     raise forms.ValidationError("手机号码不合法",code="InvalidateMobile")



