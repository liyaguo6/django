from django.db import models

# Create your models here.




# 出版社类
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    address=models.CharField(max_length=32)




# 书类
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    # 出版日期
    date = models.DateField(null=True)  # datetime.date()
    # 书只能关联一个出版社, 外键通常建在多的那一边
    publisher = models.ForeignKey(to="Publisher")




# 作者类
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    # 多对多， 建在哪边都可以
    books = models.ManyToManyField(to="Book")
