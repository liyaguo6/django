"""BMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 出版社管理
    url(r'^publisher_list/', views.publisher_list, name='publisher_list'),
    url(r'^delete_publisher/(?P<id>\d+)/', views.delete_publisher, name='delete_publisher'),
    url(r'^add_publisher/', views.add_publisher, name='add_publisher'),
    url(r'^edit_publisher/(?P<edit_id>\d+)', views.edit_publisher, name='edit_publisher'),

    # 图书管理
    url(r'^books_list/', views.books_list, name='books_list'),
    url(r'^delete_books/(?P<id>\d+)/', views.delete_books, name='delete_books'),
    url(r'^add_books/', views.add_books, name='add_books'),
    url(r'^edit_books/(?P<edit_id>\d+)', views.edit_books, name='edit_books'),

    # 作者管理
    url(r'^author_list/', views.author_list, name='author_list'),
    url(r'^delete_author/(?P<delete_id>\d+)', views.delete_author, name='delete_author'),
    url(r'^add_author/', views.add_author, name='add_author'),
    url(r'^edit_author/(?P<edit_id>\d+)', views.edit_author, name='edit_author'),

    # 登录页面
    url(r'^login/', views.login, name='login'),

]
