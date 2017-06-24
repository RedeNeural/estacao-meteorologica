# -*- coding:utf-8 -*-

import vcr

from datetime import datetime

from django.conf import settings
from django.test import TestCase

from estacaometeorologica.core.models import format_strptime_datetime
from estacaometeorologica.core.models import format_strftime_datetime
from estacaometeorologica.core.models import EstacaoMeteorologica


class EstacaoMeteorologicaTestCase(TestCase):

    @vcr.use_cassette(settings.BASE_DIR + '/estacaometeorologica/core/tests/cassettes/morangos.yaml')
    def test_update_data(self):
        EstacaoMeteorologica.objects.update_data()

        self.assertEqual(EstacaoMeteorologica.objects.count(), 987)

    @vcr.use_cassette(settings.BASE_DIR + '/estacaometeorologica/core/tests/cassettes/morangos.yaml')
    def test_get_json(self):
        EstacaoMeteorologica.objects.update_data()

        self.assertTrue(EstacaoMeteorologica.objects.get_json())

    def test_format_strftime_datetime(self):
        self.assertEqual(format_strftime_datetime(datetime(2017, 1, 1, 12, 0, 0)), '01/01/2017 12:00')

