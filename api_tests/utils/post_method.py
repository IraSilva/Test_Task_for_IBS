import random
from api_tests.utils.http_methods import HTTPMethods
from data.urls import post_create_user
from data.data import CreateUserData


class CreateUsers:
    """Методы POST для создания пользователя"""

    @staticmethod
    def post_create_new_user():
        """Метод для создания пользователя по заданному body"""
        response = HTTPMethods.post(f"{post_create_user}", data=CreateUserData.body_for_create_new_user)
        return response

    @staticmethod
    def post_create_new_user_with_empty_body():
        """Метод для создания пользователя с пустым телом запроса"""
        response = HTTPMethods.post(f"{post_create_user}", data={})
        return response

    @staticmethod
    def post_create_new_user_with_random_body():
        """Метод для создания пользователя с рандомными данными в теле запроса"""
        value1 = random.randint(1, 10)
        value2 = str(random.choice(["rus", "eng", "span", "germ", "fr", "br"]))
        user_body = {
            "key1": value1,
            "key2": value2
        }
        response = HTTPMethods.post(f"{post_create_user}", data=user_body)
        return response

