from django.db import models
from django.contrib.auth.models import User
from .constants import CITIES, REGIONS
from datetime import datetime, timedelta


class City(models.Model):
    name = models.CharField(max_length=100,
                            default=None,
                            blank=False,
                            choices=CITIES,
                            verbose_name='Город')


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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
