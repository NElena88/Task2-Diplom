import string
from datetime import date, timedelta
import random
from turtle import color

import password
from faker import Faker

fake = Faker()


def generate_create_user_body():
    password = "".join(
        random.choice(string.ascii_letters + string.digits + "!@#$%^&*")
        for _ in range(8))
    return {
        "email": fake.unique.email(),
        "password": password,
        "name": fake.user_name()
    }


