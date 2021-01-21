from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import view


router = SimpleRouter()
router.register(r'users', view.UserModelViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]