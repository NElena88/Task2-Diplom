import allure
import pytest

from generators import generate_create_user_body
from create_user_methods import CreateUserMethods
from data import MessageText


class TestCreateUser:
    @allure.title('Успешное создание уникального пользователя')
    def test_create_unique_user(self, generate_data_for_creation):
        create_user_body, email, password, name = generate_data_for_creation

        with allure.step('Проверка создания пользователя'):
            response = CreateUserMethods.create_user(email, password, name)
        with allure.step('Запрос возвращает правильный код ответа'):
            assert response.status_code == 200
        with allure.step('Успешный запрос возвращает тело ответа'):
            json_response = response.json()
            assert json_response["success"] is True
            assert "email" in json_response["user"]
            assert "name" in json_response["user"]
            assert json_response["user"]["email"] == email
            assert json_response["user"]["name"] == name
            assert json_response["accessToken"].startswith("Bearer ")
            assert isinstance(json_response["refreshToken"], str)

    @allure.title('Проверка ошибки при создании дубликата логина пользователя')
    def test_create_existing_user_show_error(self, generate_data_for_creation):
        create_user_body,email, password, name = generate_data_for_creation

        with allure.step('Создание первого пользователя'):
            response_first = CreateUserMethods.create_user(email, password, name)
            assert response_first.status_code == 200

        with allure.step('Проверка создания двух одинаковых пользователей'):
            response_duplicate = CreateUserMethods.create_user(email, password, name)

        with allure.step('Проверка вывода ошибки при дублировании логина'):
            assert response_duplicate.status_code == 403
            assert response_duplicate.json()["message"] == MessageText.LOGIN_ALREADY_USED_MSG

    @pytest.mark.parametrize("missing_field", ['email', 'password', 'name'])
    @allure.title('Проверка вывода ошибки без указания обязательных полей при создании пользователя')
    def test_create_user_missing_required_fields(self, missing_field):
        with allure.step(f'Генерация тела запроса без поля "{missing_field}"'):
            body = generate_create_user_body()
            body.pop(missing_field)

        with allure.step(f'Отправка запроса без поля "{missing_field}"'):
            response = CreateUserMethods.create_user(
                email=body.get("email", ""),
                password=body.get("password", ""),
                name=body.get("name", "")
            )

        with allure.step(f'Проверка вывода ошибки обязательных к заполнению полей "{missing_field}"'):
            assert response.status_code == 403, f"Ожидали 403, получили {response.status_code} при отсутствии {missing_field}"
            assert response.json()["message"] == MessageText.MISSING_DATA_FOR_ACCOUNT_CREATION_MSG

