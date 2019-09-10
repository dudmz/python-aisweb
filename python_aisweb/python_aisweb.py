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
        """
        This function makes the callable "attr" a param for request function.
        :param name: Name of the requested info to the API.
        :return: wrapper function that modifies behavior of getattr dunder function.
        """
        def wrapper(data=None, method='GET', response_type='XML'):
            if data is None:
                data = {}
            response = self.request(name, data, method, response_type)
            return response
        return wrapper

    def request(self, name, data, method, response_type):
        """
        This function makes the request to the API, as well as building the request for it.
        :param name: Name of the requested info to the API.
        :param data: Data to be sent as parameters to the API.
        :param method: HTTP method to be used.
        :param response_type: Type of data response. Default is XML and could be JSON.
        :return: Data response as XML OR JSON. Might be None if any Exception raises.
        """
        built_req = f'{self.__API_BASE}?apiKey={self.__API}&apiPass={self.__API_PASS}&area={name}'
        built_req += ''.join([f"&{key}={value}" for key, value in data.items()])

        if method == 'GET':
            response = requests.get(built_req)
        else:
            raise NotImplementedError(f"Error: method {method} not supported at this time!")

        if response:
            if response.status_code == 404:
                raise TypeError("Endpoint does not exist or incorrect data entry. Check the docs!")
            if response_type == 'XML':
                return response.content
            elif response_type == 'JSON':
                return self._convert_response_json(response.content)
            else:
                raise TypeError(f"Type {response_type} not supported.")
        else:
            raise TypeError("API is not responding at this time.")

    @staticmethod
    def _convert_response_json(response_content):
        """
        Converts XML data to JSON data string.
        :param response_content: XML data string.
        :return: JSON data string.
        """
        return json.dumps(xmltodict.parse(response_content), indent=4)
