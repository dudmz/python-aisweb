# -*- coding: utf-8 -*-

import requests


class AISWEB(object):

    def __init__(self, API, API_PASS):
        self.API = API
        self.API_PASS = API_PASS
        self.API_BASE = 'https://www.aisweb.aer.mil.br/api/'

    def __getattr__(self, name):

        def wrapper(data={}, method='GET'):
            response = self.request(name, data, method)
            return response

        return wrapper

    def request(self, name, data, method):

        built_req = '{}?apiKey={}&apiPass={}&area={}'.format(
            self.API_BASE, self.API, self.API_PASS, name
        )

        for key, value in data.items():
            built_req += '&{}={}'.format(key, value)

        if method == 'GET':
            response = requests.get(built_req)

        try:
            if response:
                if response.status_code == 404:
                    raise Exception(
                        "Endpoint does not exist or incorrect data entry,"
                        " check the docs!"
                    )
                else:
                    return response

        except Exception:
            raise Exception("Error: method {} not supported at this time!".format(
                method
            ))

        return