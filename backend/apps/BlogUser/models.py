from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户资料
    """
    email = models.EmailField(verbose_name="邮箱")
    point = models.IntegerField(default=0, verbose_name="积分")

    class Meta:
        verbose_name = "用户资料"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username