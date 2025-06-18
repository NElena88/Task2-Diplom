import pytest

from create_order_methods import CreateOrderMethods
from create_user_methods import CreateUserMethods
from generators import generate_create_user_body

@pytest.fixture
def generate_data_for_creation():
    create_user_body = generate_create_user_body()
    email = create_user_body["email"]
    password = create_user_body["password"]
    name = create_user_body["name"]
    yield [create_user_body, email, password, name]

    login_response = CreateUserMethods.login_user(email, password)
    if login_response.status_code == 200:
        token = CreateUserMethods.get_access_token(login_response)
        CreateUserMethods.delete_user(token)

@pytest.fixture
def generate_data_for_login():
    create_user_body = generate_create_user_body()
    email = create_user_body["email"]
    password = create_user_body["password"]
    name = create_user_body["name"]
    create_response = CreateUserMethods.create_user(email, password, name)
    assert create_response.status_code == 200

    yield [create_user_body, email, password, name]
    login_response = CreateUserMethods.login_user(email, password)
    if login_response.status_code == 200:
        token = CreateUserMethods.get_access_token(login_response)
        CreateUserMethods.delete_user(token)

@pytest.fixture
def get_ingredients():
    response = CreateOrderMethods.get_info_about_ingredients()
    assert response.status_code == 200
    return response.json()["data"]


