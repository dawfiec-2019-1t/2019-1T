from rest_framework import routers
from rest_framework_mongoengine import routers as merouters

from .views import *

router = routers.SimpleRouter()
router.register('asambleista',AsambleistaViewSet)
router.register('usuario',UsuarioViewSet)
router.register('ley',LeyViewSet)
router.register('persona',PersonaViewSet)
router.register('comentario',ComentarioViewSet)
router.register('comentarioley',ComentarioLeyViewSet)
router.register('voto',VotoViewSet)
#router.register('contactomail',contactomail)
merouter = merouters.DefaultRouter()
merouter.register(r'laws', lawsViewSet)


urlpatterns = router.urls + merouter.urls
