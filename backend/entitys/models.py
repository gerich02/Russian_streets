from datetime import datetime, timedelta

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models

from .constants import CITIES, REGIONS
from .managers import UserManager


class City(models.Model):
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


class Discipline(models.Model):
    title = models.CharField(max_length=100,
                             default=None,
                             blank=False,
                             verbose_name='Дисциплина')
    title = models.TextField(default=None,
                             verbose_name='Текст')


class Region(models.Model):
    name = models.CharField(max_length=255,
                            default=None,
                            blank=False,
                            choices=REGIONS,
                            verbose_name='Регион')


class Place(models.Model):
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


class Event(models.Model):
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


class Article(models.Model):
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


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email',
                              blank=False,
                              unique=True)
    name = models.CharField(verbose_name='Имя',
                            max_length=30,)
    surname = models.CharField(verbose_name='Фамилия',
                               max_length=30,)
    patronymic = models.CharField(verbose_name='Отчество',
                                  max_length=30,)
    phone_number = models.CharField(verbose_name='Номер телефона',
                                    max_length=12,
                                    unique=True,)
    birthdate = models.DateField(verbose_name='Дата рождения')
    city = models.ForeignKey(City,
                             null=True,
                             verbose_name='Город',
                             on_delete=models.CASCADE)
    region = models.ForeignKey(Region,
                               null=True,
                               verbose_name='Регион',
                               on_delete=models.CASCADE)
    social_network = models.CharField(verbose_name='Социальная сеть для связи',
                                      blank=True,
                                      max_length=100)
    is_staff = models.BooleanField(verbose_name='Сотрудник',
                                   default=False,)
    passport_series = models.CharField(verbose_name='Серия пасспорта',
                                       blank=True,
                                       max_length=10,
                                       unique=True,)
    passport_number = models.CharField(verbose_name='Номер пасспорта',
                                       blank=True,
                                       max_length=10,
                                       unique=True,)
    passport_giver = models.CharField(verbose_name='Кем выдан пасспорт',
                                      blank=True,
                                      max_length=255,)
    passport_date = models.DateField(verbose_name='Дата выдачи пасспорта',
                                     blank=True,)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_full_name(self):
        '''
        Возвращает ФИО.
        '''
        full_name = f'{self.name} {self.surname} {self.patronymic}'
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Отправляет электронное письмо этому пользователю.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
