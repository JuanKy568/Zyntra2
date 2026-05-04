from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, AvatarViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'avatars', AvatarViewSet)

urlpatterns = router.urls