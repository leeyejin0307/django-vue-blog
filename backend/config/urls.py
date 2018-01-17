from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token


from Blog.urls import router

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # api url
    re_path('api/v1/', include(router.urls)),
    # api login
    re_path('api-auth/', include('rest_framework.urls',
            namespace='rest_framework')),
    path('api/v1/login/', obtain_jwt_token),
]
