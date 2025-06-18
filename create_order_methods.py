import requests

from curl import Url


class CreateOrderMethods:
    @staticmethod
    def create_order(body, headers=None):
        order_response = requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER_URL}', json=body, headers=headers)
        return order_response

    @staticmethod
    def get_info_about_ingredients():
        response = requests.get(f'{Url.BASE_URL}{Url.INGREDIENTS_URL}')
        return response



