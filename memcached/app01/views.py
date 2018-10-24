from django.shortcuts import render,HttpResponse,redirect
import memcache
import time



###################自己写装饰器#########################
# Create your views here.
# def cache(func):
#     def inner(request,*args,**kwargs):
#         #打开文件，读取内容
#         mc = memcache.Client(['192.168.31.176:12000'],debug=True)
#         val=mc.get('k3')
#         if val:
#             print(val)
#             return HttpResponse(val)
#         else:
#             ret=func(request,*args,**kwargs)
#             mc.set('k3',ret)
#             return ret
#     return inner
# @cache


# @cache  #index = cache(index)
# def index(request):
#     ctime = time.time()
#     return render(request,'index.html',{'ctime':ctime})

###################单独视图缓存#########################
# from django.views.decorators.cache import cache_page
# @cache_page(5)
# def index(request):
#     ctime = time.time()
#     return render(request,'index.html',{'ctime':ctime})


#####################全站使用########################
#利用中间件
def index(request):
    ctime = time.time()
    return render(request,'index.html',{'ctime':ctime})