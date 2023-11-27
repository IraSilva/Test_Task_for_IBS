import json
import requests
from data.data import ExpectedResult


class Assertion:
    """Методы для проверки ответов на запросы"""

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, f"Фактический статус-код: {result.status_code}, " \
                                                  f"не совпадает с ожидаемым."

    @staticmethod
    def check_json_format_in_response(result):
        """Проверка, что ответ на запрос в формате JSON"""
        try:
            result.json()
        except json.JSONDecodeError:
            assert False, f"Ответ не в JSON формате. Фактический текст ответа: '{result.text}'"

    @staticmethod
    def check_keys_of_json_response(result, key):
        """Метод для проверки наличия ожидаемых ключей в ответе"""
        try:
            response = result.json()
        except json.JSONDecodeError:
            assert False, f"Ответ не в JSON формате. Фактический текст ответа: '{result.text}'"
        assert key in response, f"в ответе нет ключа: '{key}'"

    @staticmethod
    def check_support_url_in_response(result):
        """Проверка правильности url в поле support"""
        actual_url = result.json()
        expected_url = ExpectedResult.support_url
        assert actual_url["support"]["url"] == expected_url, f"Url не совпадает с ожидаемым."

    @staticmethod
    def check_support_message_in_response(result):
        """Проверка правильности сообщения 'text' в поле support"""
        actual_text = result.json()
        expected_text = ExpectedResult.support_message
        assert actual_text["support"]["text"] == expected_text, f"Текст сообщения не совпадает с ожидаемым."

    @staticmethod
    def check_avatar_url_in_response_has_status_code_200(result):
        """Проверка, что ссылка на изображение в поле 'avatar' дает ответ статус-код 200"""
        response = result.json()["data"]
        img_url = response.get("avatar")
        assert requests.get(img_url).status_code == 200, f"Переход по ссылке даёт неверный статус код."

    @staticmethod
    def check_keys_in_data_field(result, key):
        """Проверка, что в поле дата содержатся верные ключи"""
        response = result.json()["data"]
        assert key in response, f"в ответе нет ключа: '{key}'"

    @staticmethod
    def check_empty_json_response(result):
        """Проверка, что ответ на запрос в формате пустого JSON"""
        try:
            result.json()
        except json.JSONDecodeError:
            assert False, f"Ответ не в JSON формате."
        assert result.json() == {}, f"Ответ не является пустым, он содержит: {result.text}"

    @staticmethod
    def check_page_number(result, page):
        """Проверка, что номер страницы в ответе правильный"""
        response = result.json()["page"]
        assert page == response, f"Страница неверная."

    @staticmethod
    def check_number_of_objects_on_page(result):
        """Проверка, что количество объектов на странице корректное"""
        expected_quantity = int(result.json()["per_page"])
        list_objects = result.json()["data"]
        actual_quantity = len(list_objects)
        assert actual_quantity <= expected_quantity, f"Количество объектов на странице не соответствует заявленному."









