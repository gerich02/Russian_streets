from django.urls import path, include
from rest_framework import routers
from .views import (UserViewSet,
                    RegionViewSet,
                    DisciplineViewSet,
                    EventViewSet,
                    CityViewSet,
                    ArticleViewSet,
                    PlaceViewSet,
                    UserAutologinView,
                    UserAllViewSet)

router = routers.DefaultRouter()
router.register(r'users/registration', UserViewSet)
router.register(r'users', UserAllViewSet, basename='user_all')
router.register(r'regions', RegionViewSet)
router.register(r'disciplines', DisciplineViewSet)
router.register(r'events', EventViewSet)
router.register(r'cities', CityViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'places', PlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('autologin/', UserAutologinView.as_view(), name='autologin'),
]
