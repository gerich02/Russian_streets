from rest_framework import routers
from .views import (UserViewSet,
                   RegionViewSet,
                   DisciplineViewSet,
                   EventViewSet)

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'region', RegionViewSet)
router.register(r'discipline', DisciplineViewSet)
router.register(r'event', EventViewSet)
