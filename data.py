class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    REGISTER_USER_URL = '/api/auth/register'
    LOGIN_USER_URL = '/api/auth/login'
    DELETE_USER_URL = '/api/auth/user'
    CREATE_ORDER_URL = '/api/orders'
    INGREDIENTS_URL = '/api/ingredients'

class MessageText:
    INCORRECT_DATA_MSG = "email or password are incorrect"
    LOGIN_ALREADY_USED_MSG = "User already exists"
    MISSING_DATA_FOR_ACCOUNT_CREATION_MSG = "Email, password and name are required fields"
    EMPTY_ID_MSG = 'Ingredient ids must be provided'

class DataForCreateUser:
    CREATE_LOGIN_BODY = {
        "email": "",
        "password": "",
        "name": ""
    }

class DataForAuth:
    CREATE_TOKEN_BODY = {
        "email": "",
        "password": ""
    }

class DataForOrderCreation:
    CREATE_ORDER_BODY = {
        "ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]
    }
