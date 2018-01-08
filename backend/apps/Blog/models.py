from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Article(models.Model):
    """
    Blog Article
    """
    title = models.CharField(max_length=250, verbose_name="标题")
    body = models.TextField(verbose_name="正文")
    author = models.ForeignKey(User, related_name="article", verbose_name="作者"
                                , on_delete=models.CASCADE,)
    publish = models.DateTimeField(default=timezone.now, verbose_name="发布日期")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新日期")

    class Meta:
        ordering = ('-publish',)
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
