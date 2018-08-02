
from blog01.models import Userinfo
from django.forms import widgets
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS,ValidationError

class UserForm(forms.Form):
    user = forms.CharField(max_length=32,
                           label='用户名',
                           error_messages={"required":"该字段不能为空"},
                           widget=widgets.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(max_length=32, label='密码',
                          widget=widgets.PasswordInput(attrs={'class': 'form-control'},
                                                       ))
    re_pwd = forms.CharField(max_length=32, label='确认密码',
                             widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=32, label='邮箱',
                             widget=widgets.EmailInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(max_length=11, label='手机号',
                                widget=widgets.TextInput(attrs={'class': 'form-control'}))
    def clean_user(self):
        user = self.cleaned_data.get("user")
        user_obj =Userinfo.objects.filter(username=user).first()
        if not user_obj:
            return user
        else:
            raise ValidationError('该用户已注册')
    def clean(self):
        pwd = self.cleaned_data.get("pwd")
        re_pwd =self.cleaned_data.get("re_pwd")
        if pwd and re_pwd:
            if pwd == re_pwd:
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致！")
        else:
            return self.cleaned_data