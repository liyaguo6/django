"""blog URL Configuration

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
from django.views.static import serve
from django.conf.urls import url
from django.contrib import admin
from blog01 import views
from blog import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login',views.login,name='login'),
    url(r'logout/',views.logout,name='logout'),
    # url(r'index/',views.index,name='index'),
    url(r'register/',views.register,name='register'),
    #media路由
    url(r'media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT}),
    url(r'get_validCode_img/',views.get_validCode_img,name='get_validCode_img'),


    #关于个人站点url
    url(r'^(?P<username>\w+)',views.home_site),




    url(r'',views.index,name='index'),

]
