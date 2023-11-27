import requests

base_url = "https://reqres.in"


class HTTPMethods:
    """Класс содержащий мои методы для запросов"""

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        result = HTTPMethods._send(url, data, headers, cookies, "GET")
        return result

    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        result = HTTPMethods._send(url, data, headers, cookies, "POST")
        return result

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        result = HTTPMethods._send(url, data, headers, cookies, "PUT")
        return result

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        result = HTTPMethods._send(url, data, headers, cookies, "DELETE")
        return result

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f"{base_url}{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}
        if method == "GET":
            result = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            result = requests.post(url, json=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            result = requests.put(url, json=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            result = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Received method isn't valid")
        return result

