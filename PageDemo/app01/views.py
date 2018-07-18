from django.shortcuts import render
from app01 import models
import random
from django.core.paginator import Paginator,EmptyPage
# Create your views here.
def index(request,current_page):
    # for i in range(20):
    #     name = '西游记章节{}'.format(i)
    #     price1 = random.random() * 10000
    #     price = float('%.3f' % price1)
    #     print(price)
    #     models.Book.objects.create(name=name, price=price)
    book_list = models.Book.objects.all()
    # cureent_page=request.GET.get('page')
    # 分页器
    paginator=Paginator(book_list,3)
    current_page=int(current_page)
    print(paginator.num_pages)
    if paginator.num_pages >5:
        if current_page -5 <1:
            page_range=range(1,6)
        elif current_page+5 > paginator.num_pages:
            page_range = range(paginator.num_pages-4,paginator.num_pages+1)
        else:
            page_range = range(current_page-2,current_page+3)
    else:
        page_range = paginator.page_range
    try:
        cureent_page_list=paginator.page(current_page)
    # for i in cureent_page:
    #     print(i)
    except EmptyPage as e:
        cureent_page_list= paginator.page(1)
    return render(request, 'index.html',locals())
