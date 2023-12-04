import pytest
import allure
import random
from api_tests.utils.get_users_method import SingleUser, ListUsers
from api_tests.utils.assertions import Assertion
from data.data import ExpectedResult


@allure.epic("API tests for GET-method for list of users")
class TestGetListUser:
    """API тесты для списка пользователей."""
    response_keys = ExpectedResult.keys_list_users
    data_keys = ExpectedResult.data_keys

    @allure.title("test_get_list_of_users_return_status_code_200")
    def test_get_list_of_users_return_status_code_200(self):
        """Проверка, что метод Get для получения списка пользователей возвращает статус-код 200"""
        page_number = random.randint(1, 100)
        result_get = ListUsers.get_list_of_users(page_number)
        Assertion.check_status_code(result_get, 200)

    @allure.title("test_get_list_of_users_return_json_response")
    def test_get_list_of_users_return_json_response(self):
        """Проверка, что метод Get для получения списка пользователей возвращает ответ в формате JSON"""
        page_number = random.randint(1, 100)
        result_get = ListUsers.get_list_of_users(page_number)
        Assertion.check_json_format_in_response(result_get)

    @allure.title("test_get_list_of_users_return_correct_page_number")
    def test_get_list_of_users_return_correct_page_number(self):
        """Проверка, что метод Get для получения списка пользователей возвращает в ответе корректный номер страницы"""
        page_number = random.randint(1, 100)
        result_get = ListUsers.get_list_of_users(page_number)
        Assertion.check_page_number(result_get, page_number)

    @allure.title("test_get_list_of_users_has_correct_keys_in_data_field")
    @pytest.mark.parametrize("key", response_keys)
    def test_get_list_of_users_has_correct_keys_in_data_field(self, key):
        """Проверка, что ответ на Get-запрос содержит правильные ключи"""
        page_number = random.randint(1, 2)
        result_get = ListUsers.get_list_of_users(page_number)
        Assertion.check_keys_of_json_response(result_get, key)

    @allure.title("test_get_list_of_users_has_correct_quantity_of_users_on_page")
    def test_get_list_of_users_has_correct_quantity_of_users_on_page(self):
        """Проверка, что ответ на Get-запрос содержит правильное количество объектов на странице"""
        page_number = random.randint(1, 2)
        result_get = ListUsers.get_list_of_users(page_number)
        Assertion.check_number_of_objects_on_page(result_get)

    @allure.title("test_get_list_of_users_for_not_valid_page")
    def test_get_list_of_users_for_not_valid_page(self):
        """Проверка, что ответ на Get-запрос для номера страницы больше, чем в 'total_pages' возвращает 0 объектов"""
        get_pages = ListUsers.get_page_total_for_list_of_users()
        pages_total = int(get_pages.json()["total_pages"])
        exceeding_page = pages_total + random.randint(1, 100)
        result_get = ListUsers.get_list_of_users(exceeding_page)
        print(result_get.json())
        Assertion.check_number_of_objects_on_not_valid_page(result_get)


@allure.epic("API tests for GET-method for single user")
class TestGetSingleUser:
    """API тесты для одного пользователя."""
    response_keys = ["data", "support"]
    data_keys = ExpectedResult.data_keys

    @allure.title("test_get_single_user_return_status_code_200")
    def test_get_single_user_return_status_code_200(self):
        """Проверка, что метод Get для получения одного пользователя по ID возвращает статус-код 200"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_status_code(result_get, 200)

    @allure.title("test_get_single_user_has_response_in_json_format")
    def test_get_single_user_has_response_in_json_format(self):
        """Проверка, что ответ на Get-запрос приходит в формате JSON"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_json_format_in_response(result_get)

    @allure.title("test_get_single_user_has_correct_keys_in_response")
    @pytest.mark.parametrize("key", response_keys)
    def test_get_single_user_has_correct_keys_in_response(self, key):
        """Проверка, что ответ на Get-запрос содержит правильные ключи"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_keys_of_json_response(result_get, key)

    @allure.title("test_get_single_user_has_correct_keys_in_data_field")
    @pytest.mark.parametrize("key", data_keys)
    def test_get_single_user_has_correct_keys_in_data_field(self, key):
        """Проверка, что ответ на Get-запрос содержит правильные ключи в поле 'data'"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_keys_in_data_field(result_get, key)

    @allure.title("test_get_single_user_has_correct_url_in_support_key")
    def test_get_single_user_has_correct_url_in_support_key(self):
        """Проверка, что в ответе на Get-запрос ключ 'support' содержит правильный url"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_support_url_in_response(result_get)

    @allure.title("test_get_single_user_has_correct_message_in_support_key")
    def test_get_single_user_has_correct_message_in_support_key(self):
        """Проверка, что в ответе на Get-запрос ключ 'support' содержит правильный текст"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_support_message_in_response(result_get)

    @allure.title("test_get_single_user_has_correct_image_url_in_avatar_key")
    def test_get_single_user_has_correct_image_url_in_avatar_key(self):
        """Проверка, что в ответе на Get-запрос ключ 'avatar' содержит корректную ссылку"""
        result_get = SingleUser.get_single_user_by_id()
        Assertion.check_avatar_url_in_response_has_status_code_200(result_get)

    @allure.title("test_get_single_user_not_found_status_code_404")
    def test_get_single_user_not_found_status_code_404(self):
        """Проверка, что метод Get для получения пользователя с несуществующим ID возвращает статус-код 404"""
        result_get = SingleUser.get_single_user_not_found()
        Assertion.check_status_code(result_get, 404)

    @allure.title("test_get_single_user_not_found_has_empty_json_response")
    def test_get_single_user_not_found_has_empty_json_response(self):
        """Проверка, что ответ на Get-запрос для пользователя с несуществующим ID приходит в формате пустого JSON"""
        result_get = SingleUser.get_single_user_not_found()
        Assertion.check_empty_json_response(result_get)
