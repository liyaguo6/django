from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import auth  # 利用django自带的用户认证组件
from blog01.utils.vaild_code import get_vaild_code_img
from blog01.Myforms import *
from blog01.models import *
from blog01 import models
from django.urls import reverse
from django.db.models import Count


# Create your views here.
# from blog01.models import *

def login(request):
    response = {'user': None, 'msg': None}
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        vaild_code = request.POST.get('valid_code')
        vaild_code_str = request.session.get('vaild_code_str')
        if vaild_code_str.upper() == vaild_code.upper():
            user = auth.authenticate(username=user, password=pwd)
            if user:
                auth.login(request, user)  # request.user == 注册session当前登陆对象
                response['user'] = user.username
            else:
                response['msg'] = '用户名或密码错误'
        else:
            response['msg'] = '验证码错误'
        return JsonResponse(response)
    return render(request, 'login.html')


def get_validCode_img(request):
    data = get_vaild_code_img(request)
    return HttpResponse(data)


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        response = {'user': None, "msg": None}
        if form.is_valid():
            response['user'] = form.cleaned_data.get('user')
            # 生成一条用户记录
            user = form.cleaned_data.get('user')
            pwd = form.cleaned_data.get('pwd')
            telephone = form.cleaned_data.get('telephone')
            email = form.cleaned_data.get('email')
            avatar_obj = request.FILES.get("avatar")
            extra = {}
            if avatar_obj:
                extra["avatar"] = avatar_obj
            Userinfo.objects.create_user(username=user, password=pwd, email=email, telephone=telephone, **extra)
        else:
            # print(form.cleaned_data)
            # print(form.errors)
            response['msg'] = form.errors
        return JsonResponse(response)
    forms = UserForm()
    return render(request, 'register.html', locals())


def logout(request):
    auth.logout(request)  # request.session.flush()
    print(reverse("login"))
    return redirect(reverse("login"))


def index(request):
    article_list = Article.objects.all()
    return render(request, 'index.html', locals())


def home_site(request, username):
    """
    个人站点页面
    :param request:
    :param username:
    :return:
    """
    user = Userinfo.objects.filter(username=username).first()
    if not user:
        return render(request, "not-found.html")
    # 查询当前站点对象
    blog = user.blog

    # 查询用户或者当前站点对应的所有文章
    # article_list=user.article_set.all() #基于对象查询
    # article_list=Article.objects.filter(user__nid="") #基于双下划线查询正向查询按字段 ，反向查询按表名
    article_list = Article.objects.filter(user=user)

    # 每一个后的表模型.objects.values("pk").annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")
    # 每一个分类名称以及对应的文章数
    # ret=models.Category.objects.values('nid').annotate(c=Count("article__nid")).values("title","c")
    # print(ret)
    # 查询当前站点的每一个分类名称以及对应的文章数
    cate_list = Category.objects.filter(blog=blog).values("pk").annotate(c=Count('article__nid')).values_list('title', 'c')

    # 查询当前站点的每一个标签名称以及对应的文章数
    tag_list = Tag.objects.filter(blog=blog).values("pk").annotate(c=Count('article__nid')).values_list('title', 'c')
    print(tag_list)
    # 查询当前站点的每一个年月名称以及对应的文章数
    # 方式一
    # ret = models.Article.objects.extra(select={'is_recent':"create_time>'2018-07-23'"}).values("title","is_recent")
    # print(ret)
    # ret=models.Article.objects.extra(select={"y_m_date":"strftime('%%Y-%%m-%%d',create_time)"}).values("y_m_date","nid","title")
    date_list = models.Article.objects.filter(user=user).extra(select={"y_m": "strftime('%%Y-%%m',create_time)"}).values(
        "y_m").annotate(c=Count("nid")).values_list("y_m","c")
    # print(ret)
    #方式二
    # from django.db.models.functions import TruncMonth
    # ret=models.Article.objects.filter(user=user).annotate(month=TruncMonth('create_time')).values('month').annotate(c=Count('nid')).values('month','c')
    # print(ret)

    return render(request, "home_site.html",locals())
