# -*- coding: utf-8 -*-
import json

import requests
import xmltodict


class AISWEB(object):

    def __init__(self, api, api_pass):
        if not api or not api_pass:
            raise TypeError("Pass the required args: API KEY and API PASSWORD")
        elif type(api) is not str or type(api_pass) is not str:
            raise TypeError("Pass the required args as strings.")

        self.__API = api
        self.__API_PASS = api_pass
        self.__API_BASE = 'https://www.aisweb.aer.mil.br/api/'

    def __getattr__(self, name):
        def wrapper(data={}, method='GET', response_type='XML'):
            response = self.request(name, data, method, response_type)
            return response
        return wrapper

    def request(self, name, data, method, response_type):
        built_req = '{}?apiKey={}&apiPass={}&area={}'.format(
            self.__API_BASE, self.__API, self.__API_PASS, name
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

                if response_type == 'XML':
                    return response.content
                elif response_type == 'JSON':
                    return self._convert_response_json(response.content)
                else:
                    raise Exception("Type % not supported." % response_type)

        except Exception:
            raise Exception("Error: method {} not supported at this time!".format(
                method
            ))

    @staticmethod
    def _convert_response_json(response_content):
        return json.dumps(xmltodict.parse(response_content), indent=4)
