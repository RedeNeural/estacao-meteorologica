# -*- coding:utf-8 -*-

import vcr

from django.conf import settings
from django.test import TestCase
from django.urls import reverse_lazy

from estacaometeorologica.core.models import EstacaoMeteorologica
from estacaometeorologica.core.api_morangos import get_data


class IndexViewTestCase(TestCase):

    @vcr.use_cassette(settings.BASE_DIR + '/estacaometeorologica/core/tests/cassettes/morangos.yaml')
    def test_get_context_data(self):
        EstacaoMeteorologica.objects.update_data()

        self.assertEqual(EstacaoMeteorologica.objects.count(), 987)

        response = self.client.get(reverse_lazy('index'))

        self.assertTrue(response.context_data.get('temperature'))
        self.assertTrue(response.context_data.get('humidity'))
        self.assertTrue(response.context_data.get('date'))


class EstacaoMeteorologicaViewTestCase(TestCase):

    @vcr.use_cassette(settings.BASE_DIR + '/estacaometeorologica/core/tests/cassettes/morangos.yaml')
    def test_get(self):
        EstacaoMeteorologica.objects.update_data()

        response = self.client.get(reverse_lazy('estacao-meteorologica'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        content = response.json()

        self.assertTrue(content['temperature'])
        self.assertTrue(content['humidity'])
        self.assertTrue(content['date'])
