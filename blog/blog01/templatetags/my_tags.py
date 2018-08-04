from django import template
from blog01.models import *
from django.db.models import Count

register = template.Library()


@register.simple_tag
def multi_tag(x, y):
    return x + y


@register.inclusion_tag("classification.html")
def get_classification_style(username):
    user = Userinfo.objects.filter(username=username).first()
    blog = user.blog
    cate_list = Category.objects.filter(blog=blog).values("pk").annotate(c=Count('article__nid')).values_list('title',
                                                                                                              'c')
    tag_list = Tag.objects.filter(blog=blog).values("pk").annotate(c=Count('article__nid')).values_list('title', 'c')
    date_list = Article.objects.filter(user=user).extra(
        select={"y_m": "strftime('%%Y/%%m',create_time)"}).values(
        "y_m").annotate(c=Count("nid")).values_list("y_m", "c")

    return {"username":username,"blog": blog, "cate_list": cate_list, "date_list": date_list, "tag_list": tag_list}
