# -*- coding:utf-8 -*-

import requests

from django.db import models


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
