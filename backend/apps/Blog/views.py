from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, mixins

from .models import Article
from .serializers import ArticlesSerializer


class ArticlePagination(PageNumberPagination):
    """
    文章分页
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100


class ArticlesViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """
    文章:
        列表
        详情
    """
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    pagination_class = ArticlePagination
