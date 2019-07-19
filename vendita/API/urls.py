from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('leads', LeadViewSet, 'api')

urlpatterns = router.urls