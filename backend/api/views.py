from django.shortcuts import get_object_or_404
from entitys.models import (Article, City, Discipline, Event, Place, Region,
                            User)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken

from .serializers import (ArticleSerializer, CitySerializer,
                          DisciplineSerializer, EventSerializer,
                          PlaceSerializer, RegionSerializer,
                          UserAllFieldsSerializer, UserSerializer)


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


class UserAllViewSet(ModelViewSet):
    """Вьюсет для модели пользователя."""

    queryset = User.objects.all()
    serializer_class = UserAllFieldsSerializer
    permission_classes = [IsAuthenticated]


class UserAutologinView(APIView):
    """Вью для автологина пользователя."""

    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        try:
            decoded_token = AccessToken(data.get('jwt_token'))
            user_id = decoded_token.payload['user_id']
            user = get_object_or_404(User, id=user_id)
            serializer = UserSerializer(user, context={'request': request})
            return Response(
                serializer.data, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(f'{e}')
