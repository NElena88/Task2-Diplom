import pytest
import allure

from create_order_methods import CreateOrderMethods
from create_user_methods import CreateUserMethods
from data import MessageText


class TestCreateOrder:
    @allure.title('Успешное создание заказа с авторизацией')
    def test_create_order_authorized_valid_ingredients(self, generate_data_for_login, get_ingredients):
        create_user_body, email, password, name = generate_data_for_login
        login_response = CreateUserMethods.login_user(email, password)
        token = login_response.json()["accessToken"]

        ingredients = [ingredient["_id"] for ingredient in get_ingredients[:4]]
        headers = {"Authorization": token}
        response = CreateOrderMethods.create_order({"ingredients": ingredients}, headers=headers)
        with allure.step('Проверка возврата статус-кода 200 при успешном заказе с авторизацией'):
            assert response.status_code == 200

        with allure.step('Проверка возврата тела ответа сервера при успешном заказе с авторизацией'):
            json_response = response.json()
            assert json_response["success"] is True
            assert "name" in json_response
            assert "order" in json_response
            assert "number" in json_response["order"]

    @allure.title('Создание заказа без авторизации')
    def test_create_order_unauthorized(self, get_ingredients):
        ingredients = [ingredient["_id"] for ingredient in get_ingredients[:4]]
        response = CreateOrderMethods.create_order({"ingredients": ingredients})

        assert response.status_code == 200

        with allure.step('Проверка возврата тела ответа сервера при заказе без авторизации'):
            json_response = response.json()
            assert json_response["success"] is True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_no_ingredients(self, generate_data_for_login):
        create_user_body, email, password, name = generate_data_for_login
        login_response = CreateUserMethods.login_user(email, password)
        token = login_response.json()["accessToken"]

        headers = {"Authorization": token}
        response = CreateOrderMethods.create_order({"ingredients": []}, headers=headers)

        with allure.step('Проверка возврата статус-кода 400 при создании заказа без ингредиентов'):
            assert response.status_code == 400

        with allure.step('Проверка вывода сообщения об ошибке при создании заказа без ингредиентов'):
            assert response.json()["message"] == MessageText.EMPTY_ID_MSG


    @allure.title('Создание заказа с невалидными ингредиентами')
    def test_create_order_invalid_ingredients(self, generate_data_for_login):
        create_user_body, email, password, name = generate_data_for_login
        login_response = CreateUserMethods.login_user(email, password)
        token = login_response.json()["accessToken"]

        headers = {"Authorization": token}
        response = CreateOrderMethods.create_order({"ingredients": ["invalid_hash1", "invalid_hash2"]}, headers=headers)
        with allure.step('Проверка возврата статус-кода 500 при создании заказа с невалидным хешем ингредиента'):
            assert response.status_code == 500