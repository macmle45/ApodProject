import requests as req


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
