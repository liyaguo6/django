from django.db import models
from django.contrib.auth.models import AbstractUser  # 利用django自带的auth_user表


# Create your models here.


class Userinfo(AbstractUser):
    """
    用户信息
    """
    nid = models.AutoField(primary_key=True)
    telephone = models.CharField(max_length=11, null=True, unique=True)
    avatar = models.FileField(upload_to='avatars/', default='/avaters/default.png')  # 上传头像文件
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)  # 自动生成时间
    blog = models.OneToOneField(to='Blog', to_field='nid', null=True,on_delete=True)

    def __str__(self):
        return self.username


class Blog(models.Model):
    """
    博客信息（站点表）
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='个人博客标题', max_length=45)
    site = models.CharField(verbose_name='站点名称', max_length=45)
    theme = models.CharField(verbose_name='博客主题', max_length=36)

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    博主个人文章分类表
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分类标题', max_length=32)
    # 一个人可以创建多个分类，因此站点是一对多的关系（一个站点和一个用户对应多个分类）
    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid',on_delete=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标签名称', max_length=32)
    # 一个人可以创建多个分类，因此站点是一对多的关系（一个站点和一个用户对应多个分类）
    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid',on_delete=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=255, verbose_name='文章描述')
    create_time = models.DateTimeField(verbose_name='文章创建时间', auto_now_add=True)

    comment_count = models.IntegerField(default=0)
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)


    user = models.ForeignKey(verbose_name='作者', to='Userinfo', to_field='nid',on_delete=True)
    category = models.ForeignKey(to='Category', to_field='nid', null=True,on_delete=True)
    tags = models.ManyToManyField(
        to='Tag',
        through='Article2Tag',  # 手动创建第三章表
        through_fields=('article', 'tag'),
    )
    content = models.TextField()

    def __str__(self):
        return self.title


class Article2Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(verbose_name='文章', to='Article', to_field='nid',on_delete=True)
    tag = models.ForeignKey(verbose_name='标签', to='Tag', to_field='nid',on_delete=True)

    class Mate:
        unique_together = [
            ('article', 'tag'),  # 定义元类 两个字段要联合唯一
        ]

    def __str__(self):
        v = self.article.title + '---' + self.tag.title
        return v





class ArticleUpDown(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey('Userinfo', null=True,on_delete=False)
    article = models.ForeignKey('Article', null=True,on_delete=False)
    is_up = models.BooleanField(default=True)

    class Mate:
        unique_together = [
            ('article', 'user'),
        ]



class Comment(models.Model):
    """
    评论表
    """
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(verbose_name="评论文章",to='Article',to_field='nid',on_delete=False)
    user =models.ForeignKey(verbose_name='评论者',to='Userinfo',to_field='nid',on_delete=False)
    content = models.CharField(verbose_name='评论内容',max_length=100)
    create_time =models.DateTimeField(verbose_name='评论时间',auto_now_add=True)
    parent_content =models.ForeignKey(to='self',null=True,on_delete=False)

    def __str__(self):
        return self.content
