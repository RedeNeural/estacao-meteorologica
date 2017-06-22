# -*- coding:utf-8 -*-

import vcr

from django.conf import settings
from django.test import TestCase

from estacaometeorologica.core.api_morangos import get_data


class APIMorangosTestCase(TestCase):

    @vcr.use_cassette(settings.BASE_DIR + '/estacaometeorologica/core/tests/cassettes/morangos.yaml')
    def test_get_data(self):
        data = get_data()

        self.assertTrue(data)
        self.assertDictEqual(data[0], {'Id': 1, 'dt': '2017-06-15T23:55:16.3', 'hum': 72.5, 'temp': 19.1})
