from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.

def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        ret = models.Userinfo.objects.filter(user = user,pwd=pwd)
        if ret :
            response = redirect('/index/')
            response.set_cookie('is_login',True,max_age=300)
            import datetime
            date=datetime.datetime(year=2019,month=7,day=23,hour=13,minute=28)
            response.set_cookie('username',user,expires=date,path='/index/')
            return response
    return render(request,'login.html')

def index(request):
    is_login = request.COOKIES.get('is_login')
    username = request.COOKIES.get('username')
    # print(is_login)
    if is_login:
        import datetime
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        last_time=request.COOKIES.get('last_time',"")
        response = render(request,'index.html',{'username':username,'last_time':last_time})
        response.set_cookie('last_time',now)
        return response
    else:
        return redirect('/login/')


def login_session(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        ret = models.Userinfo.objects.filter(user = user,pwd=pwd)
        if ret :
            request.session['is_login'] = True
            request.session['username'] = user

            """
            1· 生成随机字符串  123
            2 · response.set_cookie('sessionid','123'
            3· 在django-session 创建记录
            """
            # response = redirect('/index/')
            # response.set_cookie('is_login',True,max_age=300)
            # import datetime
            # date=datetime.datetime(year=2019,month=7,day=23,hour=13,minute=28)
            # response.set_cookie('username',user,expires=date,path='/index/')
            return redirect('/index_session/')
    return render(request,'login.html')


def index_session(request):
    is_login=request.session.get('is_login')
    if is_login:
        import datetime
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        last_time = request.session.get('last_time', "")
        request.session['last_time'] = now
        username=request.session.get('username')
        return render(request,'index.html',{'username':username,'last_time':last_time})
    else:
        return  redirect('/login_session/')

def logout(request):

    # del request.session['is_login']
    request.session.flush()
    """
    str = request.session.get('sessionid')
    django_session.objects.filter(session_key = str).delete()
    """
    return redirect('/login_session/')