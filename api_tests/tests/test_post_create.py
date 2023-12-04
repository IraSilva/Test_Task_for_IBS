from pprint import pprint
import pytest
import allure
import random
from api_tests.utils.post_method import CreateUsers
from api_tests.utils.assertions import Assertion
from data.data import ExpectedResult


@allure.epic("API tests for POST-method for create new user")
class TestCreateUser:
    """API tests for POST-method create user."""
    response_keys = ["id", "createdAt"]

    @allure.title("")
    def test_post_method_with_any_body_request_return(self):
        """Проверка, что метод Post для создания пользователя с любым телом запроса возвращает статус-код 201"""
        result_post = CreateUsers.post_create_new_user_with_random_body()
        print(result_post.json())
        Assertion.check_status_code(result_post, 201)

    @allure.title("")
    def test_post_method_with_full_body_request_return_json_response(self):
        """Проверка, что метод Post для создания пользователя возвращает ответ в формате JSON"""
        result_post = CreateUsers.post_create_new_user_with_random_body()
        Assertion.check_json_format_in_response(result_post)

    @allure.title("")
    def test_post_method_with_empty_body_request_return_status_code_201(self):
        """Проверка, что метод Post для создания пользователя с пустым телом запроса возвращает статус-код 201"""
        result_post = CreateUsers.post_create_new_user_with_empty_body()
        Assertion.check_status_code(result_post, 201)

    @allure.title("")
    @pytest.mark.parametrize("keys", response_keys)
    def test_post_method_with_random_body_request_return_keys_id_and_created_at(self, keys):
        """Проверка, что метод Post для создания пользователя с любым телом запроса возвращает ключи id и createdAt"""
        result_post = CreateUsers.post_create_new_user_with_random_body()
        print(result_post.json())
        Assertion.check_keys_of_json_response(result_post, keys)






