from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from .serializers import UserProfileSerializer

User = get_user_model()

class BasePagination(PageNumberPagination):
    """
    分页
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class UserProfileViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """
    用户资料:
        详情
        列表
    """
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = BasePagination
    lookup_field = 'username'
