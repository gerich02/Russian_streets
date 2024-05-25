from entitys.models import (City,
                            Discipline,
                            Region,
                            Place,
                            Event,
                            Article,
                            User)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken


class ArticleSerializer(serializers.ModelSerializer):
    """Сериализатор модели Article."""

    class Meta:
        """Meta."""

        model = Article
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    """Сериализатор модели Place."""

    class Meta:
        """Meta."""

        model = Place
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    """Сериализатор модели City."""

    class Meta:
        """Meta."""

        model = City
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор модели Event."""

    class Meta:
        """Meta."""

        model = Event
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    """Сериализатор модели Region."""

    class Meta:
        """Meta."""

        model = Region
        fields = '__all__'


class DisciplineSerializer(serializers.ModelSerializer):
    """Сериализатор модели Discipline."""

    class Meta:
        """Meta."""

        model = Discipline
        fields = '__all__'


class UserAllFieldsSerializer(serializers.ModelSerializer):
    """Сериализатор модели User, возвращающий все поля."""

    class Meta:
        """Meta."""

        model = User
        fields = '__all__'
        ref_name = 'CustomBaseUser'


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User."""

    jwt = serializers.SerializerMethodField()

    class Meta:
        """Meta."""

        model = User
        fields = ['name',
                  'region',
                  'email',
                  'password',
                  'phone_number',
                  'social_network',
                  'jwt']
        ref_name = 'CustomUser'

    def get_jwt(self, obj):
        token = AccessToken.for_user(self.context['request'].user)
        return str(token)
