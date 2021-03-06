# -*- coding:utf-8 -*-

import requests

from datetime import datetime

from django.db import models
from django.utils import timezone

from estacaometeorologica.core.api_morangos import get_data


def format_strptime_datetime(dt):
    try:
        dt = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        dt = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        dt = timezone.now()

    return dt

def format_strftime_datetime(dt):
    return dt.strftime('%d/%m/%Y %H:%M')


class EstacaoMeteorologicaManager(models.Manager):

    def update_data(self):
        data = get_data()

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
        context = {}

        context['temperature'] = []
        context['humidity'] = []
        context['date'] = []

        for obj in self.all():
            context['temperature'].append(float(obj.temperature))
            context['humidity'].append(float(obj.humidity))
            context['date'].append(format_strftime_datetime(obj.date))

        return context


class EstacaoMeteorologica(models.Model):

    class Meta:
        verbose_name = 'Estação Meteorológica'
        verbose_name_plural = 'Estação Meteorológica'

    identifier = models.PositiveIntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EstacaoMeteorologicaManager()
