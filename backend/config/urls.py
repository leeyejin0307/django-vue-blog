from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from Blog.views import ArticlesViewset


router = DefaultRouter()

# 文章
router.register(r'post', ArticlesViewset, base_name="article")


urlpatterns = [
    path('admin/', admin.site.urls),
    # api url
    re_path('api/v1/', include(router.urls)),
    # api login
    re_path('api-auth/', include('rest_framework.urls',
            namespace='rest_framework'))
]
