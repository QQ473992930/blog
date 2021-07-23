from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):

    #手机号
    mobile = models.IntegerField(max_length=11,blank=False,unique=True)
    #头像信息
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    #个人简介
    user_desc= models.CharField(max_length=300,blank=True)

    # 修改认证的字段为 手机号
    USERNAME_FIELD = 'mobile'

    # 创建超级管理员必须输入的字段（不包括 手机号和密码）
    REQUIRED_FIELDS = ['username', 'email']


    class Meta:
        db_table='tb_users'
        verbose_name='用户管理'
        verbose_name_plural=verbose_name #admin后台显示

    def __str__(self):
        return self.mobile

