from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import filters

from .models import Article, Comment, Category
from .serializers import ArticlesSerializer, CommentsSerializer, CategorysSerializer


class BasePagination(PageNumberPagination):
    """
    分页
    """
    page_size = 10
    page_size_query_param = 'page_size'
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
    pagination_class = BasePagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = ('created', 'views')
    search_fields = ('category__text', )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # 统计文章阅读量
        instance.increase_views()
        return Response(serializer.data)


class CommentsViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """
    评论:
        列表
        详情
    """
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    pagination_class = BasePagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('article__id',)


class CategorysViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """
    种类:
        列表
        详情
    """
    queryset = Category.objects.all()
    serializer_class = CategorysSerializer
    pagination_class = BasePagination
    ordering_fields = ('created', 'views')
    search_fields = ('category__id')
