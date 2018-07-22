from django.shortcuts import render,HttpResponse
from app01.myforms import *
# Create your views here.


def reg(request):
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)  # 所有干净的字段以及对应的值
            return HttpResponse('OK')
        else:
            print(forms.cleaned_data)  #
            print(forms.errors)  # ErrorDict : {"校验错误的字段":["错误信息",]}
            print(forms.errors.get("name"))  # ErrorList ["错误信息",]
            # 全局钩子错误
            print(forms.errors.get('__all__')[0])
            errors_all =forms.errors.get('__all__')
            return render(request, "register.html", locals())
    forms = UserForm()
    return render(request, "register.html", locals())
