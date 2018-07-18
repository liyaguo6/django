from django.shortcuts import render,HttpResponse
from app01 import models

# Create your views here.
def index(request):


    return render(request,'index.html')

def test_ajax(request):


    return HttpResponse('hello ajax')

def cal(request):
    n1 =request.POST.get('n1')
    n2 =request.POST.get('n2')
    return HttpResponse(n1+n2)


def login(request):
    # data=models.User.objects.all()
    user =request.POST.get('user')
    pwd =request.POST.get('pwd')
    data=models.User.objects.filter(name=user,pwd=pwd).first()
    res = {'user':None,'msg':None}
    if data:
        res['user']=data.name
    else:
        res['msg'] = 'username or password error!'
    import json
    print(json.dumps(res))  #{"user": null, "msg": "username or password error!"}
    print(type(json.dumps(res)))    #<class 'str'>
    return HttpResponse(json.dumps(res))

def filepush(request):
    if request.method == 'POST':
        # print(request.POST)  # contentType ==urlencoded ,request.Post才有数据
        print('body',request.body)  #请求报文中请求体数据
        print('post',request.POST)
        print(request.FILES)
        file_obj = request.FILES.get('file')
        with open('.//pic//{}'.format(file_obj.name),'wb') as f :
            for line in file_obj:
                f.write(line)
        return HttpResponse('ok')
    return render(request,'filepush.html')