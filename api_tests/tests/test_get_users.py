"""API tests for GET-method for Users."""

from pprint import pprint
import pytest
import random
from api_tests.utils.get_users_method import SingleUser, ListUsers
from api_tests.utils.assertions import Assertion
from data.data import ExpectedResult


class TestGetListUser:
    """API tests for GET-method for list of users."""
    response_keys = ExpectedResult.keys_list_users
    data_keys = ExpectedResult.data_keys

    def test_get_list_of_users_return_status_code_200(self):
        """Проверка, что метод Get для получения списка пользователей возвращает статус-код 200"""
        page_number = random.randint(1, 100)
        result_get = ListUsers.get_list_of_users(page_number)
        pprint(result_get.json())
        Assertion.check_status_code(result_get, 200)

    def test_get_list_of_users_return_json_response(self):
        """Проверка, что метод Get для получения списка пользователей возвращает ответ в формате JSON"""
        page_number = random.randint(1, 100)
        result_get = ListUsers.get_list_of_users(page_number)
        Assertion.check_json_format_in_response(result_get)

    def test_get_list_of_users_return_correct_page_number(self):
        """Проверка, что метод Get для получения списка пользователей возвращает в ответе корректный номер страницы"""
        page_number = random.randint(1, 100)
        result_get = ListUsers.get_list_of_users(page_number)
        Assertion.check_page_number(result_get, page_number)

    @pytest.mark.parametrize("key", response_keys)
    def test_get_list_of_users_has_correct_keys_in_data_field(self, key):
        """Проверка, что ответ на Get-запрос содержит правильные ключи"""
        page_number = random.randint(1, 2)
        result_get = ListUsers.get_list_of_users(page_number)
        Assertion.check_keys_of_json_response(result_get, key)

    def test_get_list_of_users_has_correct_quantity_of_users(self):
        """Проверка, что ответ на Get-запрос содержит правильное количество объектов на странице"""
        page_number = random.randint(1, 2)
        result_get = ListUsers.get_list_of_users(page_number)
        Assertion.check_number_of_objects_on_page(result_get)


class TestGetSingleUser:
    """API tests for GET-method for single user."""
    response_keys = ["data", "support"]
    data_keys = ExpectedResult.data_keys

    def test_get_single_user_return_status_code_200(self):
        """Проверка, что метод Get для получения одного пользователя по ID возвращает статус-код 200"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_status_code(result_get, 200)

    def test_get_single_user_has_response_in_json_format(self):
        """Проверка, что ответ на Get-запрос приходит в формате JSON"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_json_format_in_response(result_get)

    @pytest.mark.parametrize("key", response_keys)
    def test_get_single_user_has_correct_keys_in_response(self, key):
        """Проверка, что ответ на Get-запрос содержит правильные ключи"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_keys_of_json_response(result_get, key)

    @pytest.mark.parametrize("key", data_keys)
    def test_get_single_user_has_correct_keys_in_data_field(self, key):
        """Проверка, что ответ на Get-запрос содержит правильные ключи в поле 'data'"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_keys_in_data_field(result_get, key)

    def test_get_single_user_has_correct_url_in_support_key(self):
        """Проверка, что в ответе на Get-запрос ключ 'support' содержит правильный url"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_support_url_in_response(result_get)

    def test_get_single_user_has_correct_message_in_support_key(self):
        """Проверка, что в ответе на Get-запрос ключ 'support' содержит правильный текст"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_support_message_in_response(result_get)

    def test_get_single_user_has_correct_image_url_in_avatar_key(self):
        """Проверка, что в ответе на Get-запрос ключ 'avatar' содержит корректную ссылку"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_avatar_url_in_response_has_status_code_200(result_get)

    def test_get_single_user_not_found_status_code_404(self):
        """Проверка, что метод Get для получения пользователя с несуществующим ID возвращает статус-код 404"""
        result_get = SingleUser.get_single_user_not_found()
        Assertion.check_status_code(result_get, 404)

    def test_get_single_user_not_found_has_empty_json_response(self):
        """Проверка, что ответ на Get-запрос для пользователя с несуществующим ID приходит в формате пустого JSON"""
        result_get = SingleUser.get_single_user_not_found()
        Assertion.check_empty_json_response(result_get)
