# -*- coding:utf-8 -*-

import requests


def get_data():
    response = requests.get('http://misoftware.com.br/Morangos/TmpHTJson')

    return response.json()
