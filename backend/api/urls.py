from rest_framework import routers
from .views import (UserViewSet,
                   RegionViewSet,
                   DisciplineViewSet,
                   EventViewSet,
                   CityViewSet,
                   ArticleViewSet,
                   PlaceViewSet)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'disciplines', DisciplineViewSet)
router.register(r'events', EventViewSet)
router.register(r'cities', CityViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'places', PlaceViewSet)
