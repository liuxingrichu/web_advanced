from django.db import models


# Create your models here.

# 创建的数据库表单名：app02_userinfo
class UserInfo(models.Model):
    # 默认创建ID列，自增， 主键
    # 用户名列，字符串类型，指定长度
    # 字符串、数字、时间、二进制
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, null=True)
    user_group = models.ForeignKey("UserGroup", to_field="uid")
    user_type_choices = (
        (1, "超级用户"),
        (2, "管理员"),
        (3, "普通用户"),
    )
    user_type_id = models.IntegerField(choices=user_type_choices, default=3)


class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32)
    ctime = models.DateTimeField(auto_now_add=True, null=True)
    uptime = models.DateTimeField(auto_now=True, null=True)
