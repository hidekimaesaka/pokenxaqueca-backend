from os import getenv

from requests import get


class NasaInterface:
    def __init__(self):
        self.api_key = getenv('NASA_API_KEY')
        self.apod_api_url = getenv('NASA_APOD_API')

    def get_apod(self):
        """
        APOD stands for Astronomy Picture Of the Day

        """
        params = {'api_key': self.api_key}

        return get(self.apod_api_url, params=params).json().get('url')
