from datetime import datetime, timedelta

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models

from .constants import CITIES, REGIONS
from .managers import UserManager


class City(models.Model):
    """Модель города."""

    name = models.CharField(max_length=100,
                            default=None,
                            blank=False,
                            choices=CITIES,
                            verbose_name='Город')

    coords_latitude = models.CharField(max_length=100,
                                       default=None,
                                       blank=False,
                                       verbose_name='Широта')

    coords_longitude = models.CharField(max_length=100,
                                        default=None,
                                        blank=False,
                                        verbose_name='Долгота')

    def __str__(self):
        """Возвращает имя обьекта."""
        return self.name


class Discipline(models.Model):
    """Модель спортивной дисциплины."""

    title = models.CharField(max_length=100,
                             default=None,
                             blank=False,
                             verbose_name='Дисциплина')
    text = models.TextField(default=None,
                            verbose_name='Текст')

    def __str__(self):
        """Возвращает имя обьекта."""
        return self.title


class Region(models.Model):
    """Модель региона."""

    name = models.CharField(max_length=255,
                            default=None,
                            blank=False,
                            choices=REGIONS,
                            verbose_name='Регион')

    def __str__(self):
        """Возвращает имя обьекта."""
        return self.name


class Place(models.Model):
    """Модель места проведения мероприятия."""

    title = models.CharField(max_length=100,
                             default=None,
                             blank=False,
                             verbose_name='Название')
    discipline = models.ForeignKey(Discipline,
                                   default=None,
                                   verbose_name='Дисциплина',
                                   blank=False,
                                   on_delete=models.CASCADE)
    city = models.ForeignKey(City,
                             default=None,
                             verbose_name='Город',
                             blank=False,
                             on_delete=models.CASCADE)
    address = models.TextField(default=None,
                               verbose_name='Адрес',
                               blank=False)

    def __str__(self):
        """Возвращает имя обьекта."""
        return self.title


class Event(models.Model):
    """Модель мероприятия."""

    title = models.CharField(max_length=100,
                             default=None,
                             blank=False,
                             verbose_name='Название')
    discipline = models.ForeignKey(Discipline,
                                   default=None,
                                   verbose_name='Дисциплина',
                                   on_delete=models.CASCADE)
    start_date_time = models.DateTimeField(verbose_name='Дата начала',
                                           default=datetime.now(),
                                           blank=False)
    end_date_time = models.DateTimeField(
        verbose_name='Дата окончания',
        default=(datetime.now() + timedelta(hours=5)),
        blank=False)
    region = models.ForeignKey(Region,
                               default=None,
                               blank=False,
                               verbose_name='Регион',
                               on_delete=models.CASCADE)
    city = models.ForeignKey(City,
                             default=None,
                             blank=False,
                             verbose_name='Город',
                             on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает имя обьекта."""
        return self.title


class Article(models.Model):
    """Модель статьи."""

    title = models.CharField(max_length=150,
                             default=None,
                             blank=False,
                             verbose_name='Название')
    pubdate = models.DateTimeField(default=datetime.now(),
                                   verbose_name='Дата публикации')
    source = models.CharField(max_length=150,
                              default=None,
                              blank=False,
                              verbose_name='Источник')
    text = models.TextField(default=None,
                            blank=False,
                            verbose_name='Текст')
    views = models.IntegerField(default=0,
                                verbose_name='Просмотры')
    discipline = models.ForeignKey(Discipline,
                                   default=None,
                                   verbose_name='Дисциплина',
                                   on_delete=models.CASCADE)
    region = models.ForeignKey(Region,
                               default=None,
                               blank=False,
                               verbose_name='Регион',
                               on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает имя обьекта."""
        return self.title


class User(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя."""

    email = models.EmailField(verbose_name='Email',
                              blank=False,
                              unique=True)
    name = models.CharField(verbose_name='Имя',
                            max_length=30,
                            blank=True,
                            null=True,
                            default=None,)
    surname = models.CharField(verbose_name='Фамилия',
                               max_length=30,
                               blank=True,
                               null=True,
                               default=None,)
    patronymic = models.CharField(verbose_name='Отчество',
                                  max_length=30,
                                  blank=True,
                                  null=True,
                                  default=None,)
    phone_number = models.CharField(verbose_name='Номер телефона',
                                    max_length=12,
                                    unique=True,
                                    blank=True,
                                    null=True,
                                    default=None,)
    birthdate = models.DateField(verbose_name='Дата рождения',
                                 blank=True,
                                 null=True,
                                 default=None,)
    city = models.ForeignKey(City,
                             null=True,
                             verbose_name='Город',
                             on_delete=models.CASCADE,
                             blank=True,
                             default=None,)
    region = models.ForeignKey(Region,
                               null=True,
                               verbose_name='Регион',
                               on_delete=models.CASCADE,
                               blank=True,
                               default=None,)
    social_network = models.CharField(verbose_name='Социальная сеть для связи',
                                      blank=True,
                                      null=True,
                                      default=None,
                                      max_length=100)
    is_staff = models.BooleanField(verbose_name='Сотрудник',
                                   default=False,)
    passport_series = models.CharField(verbose_name='Серия пасспорта',
                                       blank=True,
                                       null=True,
                                       max_length=10,
                                       unique=True,
                                       default=None,)
    passport_number = models.CharField(verbose_name='Номер пасспорта',
                                       blank=True,
                                       null=True,
                                       max_length=10,
                                       unique=True,
                                       default=None,)
    passport_giver = models.CharField(verbose_name='Кем выдан пасспорт',
                                      blank=True,
                                      null=True,
                                      max_length=255,
                                      default=None,)
    passport_date = models.DateField(verbose_name='Дата выдачи пасспорта',
                                     blank=True,
                                     null=True,
                                     default=None,)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        """Meta."""

        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_full_name(self):
        """Возвращает ФИО."""
        full_name = f'{self.name} {self.surname} {self.patronymic}'
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Отправляет электронное письмо этому пользователю."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
