# -*- coding:utf-8 -*-

import requests

from datetime import datetime

from django.db import models
from django.utils import timezone


def format_strptime_datetime(dt):
    try:
        dt = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        dt = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        dt = timezone.now()

    return dt

def format_strftime_datetime(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')


class EstacaoMeteorologicaManager(models.Manager):

    def update_data(self, data):
        for info in data:
            identifier = info.get('Id')

            if not self.filter(identifier=identifier).exists():
                self.create(
                    identifier=identifier,
                    temperature=info.get('temp'),
                    humidity=info.get('hum'),
                    date=format_strptime_datetime(info.get('dt'))
                )

    def get_json(self):
        object_list = []

        for obj in self.all():
            object_list.append({
                'identifier': obj.identifier,
                'temperature': obj.temperature,
                'humidity': obj.humidity,
                'date': format_strftime_datetime(obj.date),
            })

        return object_list


class EstacaoMeteorologica(models.Model):

    class Meta:
        verbose_name = 'Estação Meteorológica'
        verbose_name_plural = 'Estação Meteorológica'

    identifier = models.PositiveIntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EstacaoMeteorologicaManager()
