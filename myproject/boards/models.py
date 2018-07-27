from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#simliar SQL building
class Board(models.Model):
    name=models.CharField(max_length=30,unique=True)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject=models.CharField(max_length=225)
    last_updated=models.DateTimeField(auto_now_add=True)
    board=models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    starter=models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)


class Post(models.Model):
    message=models.TextField(max_length=4000)
    topic=models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)

    """创建Post对象时，将使用当前日期和时间"""
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(null=True)
    updated_by=models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)

    """created_by 是外键字段，
    关联的User模型，表明这个帖子是谁创建的，
    related_name=posts 表示在 User 那边可以使用 user.posts 来查看这个用户创建了哪些帖子"""
    created_by=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    updated_by=models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)


# board=Board(name='Django',description='This is a board about Django')
# board.save()

