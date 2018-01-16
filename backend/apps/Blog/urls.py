from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

# 文章
router.register(r'posts', views.ArticlesViewset, base_name="article")
router.register(r'comments', views.CommentsViewset, base_name="comment")
router.register(r'categorys', views.CategorysViewset, base_name="category")
