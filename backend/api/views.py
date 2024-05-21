from . serializers import (UserSerializer,
                         EventSerializer,
                         RegionSerializer,
                         DisciplineSerializer)
from rest_framework.viewsets import ModelViewSet
from entitys.models import (Region, Discipline, Event, User)


class RegionViewSet(ModelViewSet):
    """
    Вьюсет для модели региона
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = []


class DisciplineViewSet(ModelViewSet):
    """
    Вьюсет для модели дисциплины
    """
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = []


class EventViewSet(ModelViewSet):
    """
    Вьюсет для модели мероприятия
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = []


class UserViewSet(ModelViewSet):
    """
    Вьюсет для модели региона
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
