from data import DataForOrderCreation


def modify_create_order_body(key, value):
    body = DataForOrderCreation.CREATE_ORDER_BODY.copy()
    body[key] = value
    return body
