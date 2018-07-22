from django import forms
from django.forms import widgets
from app01.models import *
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class UserForm(forms.Form):
    name = forms.CharField(min_length=5, label='姓名', error_messages={'required': '该字段不能为空'},
                           widget=widgets.TextInput(attrs={"class": 'form-control'}))
    email = forms.EmailField(label='邮箱', error_messages={'required': '不能为空', 'invaild': '格式错误'},
                             widget=widgets.TextInput(attrs={"class": 'form-control'}))
    pwd = forms.CharField(min_length=5,label='密码', widget=widgets.PasswordInput(attrs={"class": 'form-control'}))
    r_pwd = forms.CharField(label='确认密码', widget=widgets.PasswordInput(attrs={"class": 'form-control'}))

    def clean_name(self):  #局部钩子
        val = self.cleaned_data.get('name')
        ret = UserInfo.objects.filter(name=val)
        print(ret)  #<QuerySet [<UserInfo: UserInfo object>]>
        if not ret:
            # print(val)
            return val
        else:
            raise ValidationError('该用户已注册')
    def clean(self):
        pwd=self.cleaned_data.get('pwd')
        r_pwd=self.cleaned_data.get('r_pwd')
        if pwd and r_pwd:
            if pwd == r_pwd:
                return self.cleaned_data
            else:
                raise ValidationError('密码不一致')
        else:
            return self.cleaned_data