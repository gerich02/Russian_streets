from . serializers import (UserSerializer,
                         EventSerializer,
                         RegionSerializer,
                         DisciplineSerializer,
                         ArticleSerializer,
                         CitySerializer,
                         PlaceSerializer)
from rest_framework.viewsets import ModelViewSet
from entitys.models import (Region,
                            Discipline,
                            Event,
                            User,
                            City,
                            Place,
                            Article)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


class CityViewSet(ModelViewSet):
    """
    Вьюсет для модели города.
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]


class PlaceViewSet(ModelViewSet):
    """
    Вьюсет для модели места.
    """

    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]


class ArticleViewSet(ModelViewSet):
    """
    Вьюсет для модели статьи.
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


class RegionViewSet(ModelViewSet):
    """
    Вьюсет для модели региона.
    """

    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [IsAuthenticated]


class DisciplineViewSet(ModelViewSet):
    """
    Вьюсет для модели дисциплины.
    """

    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticated]


class EventViewSet(ModelViewSet):
    """
    Вьюсет для модели мероприятия.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(ModelViewSet):
    """Вьюсет для модели пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
