from django.urls import path
from rest_framework.routers import SimpleRouter

from drfapp.views import ProductViewSet,BookViewSet
from drfapp.views.toy_views import toy_view

urlpatterns = [
    path('toys/<int:toyid>/',toy_view),
]

router = SimpleRouter()
router.register(r'products',ProductViewSet)
router.register(r'books',BookViewSet)

urlpatterns += router.urls   # 拼接路由集