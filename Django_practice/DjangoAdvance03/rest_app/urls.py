from rest_framework.routers import SimpleRouter

from rest_app.views import ArticleViewSet

router = SimpleRouter()
router.register(r'articles',ArticleViewSet)   # 将视图集与路由关联