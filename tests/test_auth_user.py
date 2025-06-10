import allure
from data import MessageText
from create_user_methods import CreateUserMethods


class TestAuthUser:
    @allure.title('Проверка успешной авторизации пользователя')
    def test_success_auth_user_login(self, generate_data_for_login):
        create_user_body, email, password, name = generate_data_for_login
        response = CreateUserMethods.login_user(email, password)
        with allure.step('Проверка возврата статус-кода 200 при успешной авторизации'):
            assert response.status_code == 200
        with allure.step('Проверка возврата тела ответа сервера при успешной авторизации'):
            json_response = response.json()
            assert json_response["success"] is True
            assert json_response["accessToken"].startswith("Bearer ")
            assert isinstance(json_response["refreshToken"], str)

            assert "email" in json_response["user"]
            assert "name" in json_response["user"]

            assert json_response["user"]["email"] == email
            assert json_response["user"]["name"] == name

    @allure.title('Проверка авторизации пользователя без заполнения одного из обязательных полей')
    def test_auth_missing_email_show_error(self, generate_data_for_login):
        with allure.step('Проверка вывода статус-кода 401 при авторизации без почты'):
            create_user_body, email, password, name = generate_data_for_login
            response = CreateUserMethods.login_user(email=None, password=password)
        assert response.status_code == 401

        with allure.step('Проверка вывода сообщения об ошибке при авторизации без почты'):
            assert response.json()["message"] == MessageText.INCORRECT_DATA_MSG

    @allure.title('Проверка авторизации пользователя без заполнения одного из обязательных полей')
    def test_auth_missing_password_show_error(self, generate_data_for_login):
        with allure.step('Проверка вывода статус-кода 401 при авторизации без пароля'):
            create_user_body, email, password, name = generate_data_for_login
            response = CreateUserMethods.login_user(email=email, password=None)
            assert response.status_code == 401

        with allure.step('Проверка вывода сообщения об ошибке при авторизации без пароля'):
            assert response.json()["message"] == MessageText.INCORRECT_DATA_MSG

    @allure.title('Проверка вывода ошибки при авторизации с неправильными логином или паролем')
    def test_user_login_wrong_credentials(self, generate_data_for_login):
        create_courier_body, email, password, name = generate_data_for_login
        response = CreateUserMethods.login_user(email=email, password='wrongpassword')
        with allure.step('Проверка вывода статус-кода 401 при авторизации с неправильным паролем'):
            assert response.status_code == 401
        with allure.step('Проверка вывода сообщения об ошибке при авторизации с неправильным паролем'):
            assert response.json()["message"] == MessageText.INCORRECT_DATA_MSG

    @allure.title('Проверка вывода ошибки при авторизации несуществующего пользователя')
    def test_login_nonexistent_user(self):
        response = CreateUserMethods.login_user(email='nonexistentuser123', password='anyPassword123')
        with allure.step('Проверка вывода статус-кода 401 при авторизации несуществуюшего пользователя'):
            assert response.status_code == 401
        with allure.step('Проверка вывода сообщения об ошибке при авторизации несуществуюшего пользователя'):
            assert response.json()["message"] == MessageText.INCORRECT_DATA_MSG


