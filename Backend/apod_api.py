import requests as req
import json


class ApodAPI:
    @staticmethod
    def download_apod_data(url, params):
        result = req.get(
            url,
            params
        )

        status = result.status_code
        if status == 200:
            return result
        else:
            raise ConnectionError(f'Error was thrown during downloading data from API\nStatus code: {status}')

    @staticmethod
    def retrieve_json_data(json_data):
        apod_data = dict()

        apod_data['date'] = json_data['date']
        apod_data['title'] = json_data['title']
        apod_data['description'] = json_data['explanation']
        apod_data['media_type'] = json_data['media_type']
        apod_data['media_hdurl'] = json_data['hdurl']

        try:
            apod_data['copyright'] = json_data['copyright']

            return apod_data
        except KeyError:
            return apod_data
