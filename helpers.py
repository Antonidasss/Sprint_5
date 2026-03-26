import random
import string
import requests
from constants import BASE_URL, API_REGISTER

def generate_user_data():
    """Генерирует случайные данные для регистрации"""
    first_name = "Anton"
    last_name = "Zakupnev"
    cohort = "42"
    random_digits = ''.join(random.choices(string.digits, k=3))
    email = f"{first_name}_{last_name}_{cohort}_{random_digits}@yandex.ru"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    name = "Test User"
    return {"email": email, "password": password, "name": name}

def create_user_via_api(user_data):
    """Отправляет запрос на регистрацию пользователя через API"""
    payload = {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"]
    }
    response = requests.post(f"{BASE_URL}{API_REGISTER}", json=payload)
    if response.status_code == 200:
        data = response.json()
        return {
            "email": user_data["email"],
            "password": user_data["password"],
            "name": user_data["name"],
            "accessToken": data.get("accessToken"),
            "refreshToken": data.get("refreshToken")
        }
    else:
        raise Exception(f"Failed to create user via API: {response.text}")