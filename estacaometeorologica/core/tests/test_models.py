# -*- coding:utf-8 -*-

import vcr

from datetime import datetime

from django.conf import settings
from django.test import TestCase

from estacaometeorologica.core.models import format_strptime_datetime
from estacaometeorologica.core.models import format_strftime_datetime
from estacaometeorologica.core.models import EstacaoMeteorologica
from estacaometeorologica.core.api_morangos import get_data


class EstacaoMeteorologicaTestCase(TestCase):

    @vcr.use_cassette(settings.BASE_DIR + '/estacaometeorologica/core/tests/cassettes/morangos.yaml')
    def test_update_data(self):
        EstacaoMeteorologica.objects.update_data(get_data())

        self.assertEqual(EstacaoMeteorologica.objects.count(), 849)

    @vcr.use_cassette(settings.BASE_DIR + '/estacaometeorologica/core/tests/cassettes/morangos.yaml')
    def test_get_json(self):
        EstacaoMeteorologica.objects.update_data(get_data())

        self.assertTrue(EstacaoMeteorologica.objects.get_json())

    def test_format_strptime_datetime(self):
        # format_strptime_datetime
        pass

    def test_format_strftime_datetime(self):
        self.assertEqual(format_strftime_datetime(datetime(2017, 1, 1, 12, 0, 0)), '2017-01-01T12:00:00')
