from rest_framework.routers import SimpleRouter

from homework_app.views import StudentViewSet

router = SimpleRouter()
router.register(r'students',StudentViewSet)