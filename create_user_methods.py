import requests

from curl import Url
from data import DataForCreateUser
from generators import *


class CreateUserMethods:
    @staticmethod
    def create_user(email, password, name):
        data = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(f'{Url.BASE_URL}{Url.REGISTER_USER_URL}', json=data)
        return response

    @staticmethod
    def login_user(email, password):
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_USER_URL}', json={"email": email, "password": password})
        return response

    @staticmethod
    def get_access_token(login_response):
        return login_response.json().get("accessToken", "").replace("Bearer ", "")

    @staticmethod
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_USER_URL}', headers=headers)




