import random
from api_tests.utils.http_methods import HTTPMethods
from data.urls import get_single_user, get_list_of_users


class ListUsers:
    @staticmethod
    def get_list_of_users(list_number):
        """Метод для get-запроса на получение списка пользователей"""
        # list_number = random.randint(1, 100)
        response = HTTPMethods.get(f"{get_list_of_users}{list_number}")
        return response


class SingleUser:
    @staticmethod
    def get_single_user_by_id():
        """Метод для get-запроса по случайному существующему ID пользователя"""
        user_id = random.randint(1, 12)
        response = HTTPMethods.get(f"{get_single_user}{user_id}")
        return response

    @staticmethod
    def get_single_user_not_found():
        """Метод для get-запроса по случайному несуществующему ID пользователя"""
        user_id = random.randint(13, 100)
        response = HTTPMethods.get(f"{get_single_user}{user_id}")
        return response
