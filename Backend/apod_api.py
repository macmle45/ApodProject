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

        raw_data = json.loads(json_data.text)

        apod_data['date'] = raw_data['date']
        apod_data['title'] = raw_data['title']
        apod_data['description'] = raw_data['explanation']
        apod_data['media_type'] = raw_data['media_type']
        apod_data['media_hdurl'] = raw_data['hdurl']

        try:
            apod_data['copyright'] = raw_data['copyright']

            return apod_data
        except KeyError:
            return apod_data
