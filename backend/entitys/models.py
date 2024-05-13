from django.db import models
from constants import CITIES, REGIONS


class City(models.Model):
    name = models.CharField(max_length=100,
                            default=None,
                            choices=CITIES,
                            verbose_name='Город')


class Discipline(models.Model):
    title = models.CharField(max_length=100,
                             default=None,
                             verbose_name='Дисциплина')
    title = models.TextField(default=None,
                             verbose_name='Текст')


class Region(models.Model):
    name = models.CharField(max_length=255,
                            default=None,
                            choices=REGIONS,
                            verbose_name='Регион')


class Place(models.Model):
    pass
