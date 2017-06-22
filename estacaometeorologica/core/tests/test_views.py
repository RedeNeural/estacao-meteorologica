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
        EstacaoMeteorologica.objects.update_data(get_data())

        self.assertEqual(EstacaoMeteorologica.objects.count(), 849)

        response = self.client.get(reverse_lazy('index'))

        self.assertTrue(response.context_data.get('data'))
