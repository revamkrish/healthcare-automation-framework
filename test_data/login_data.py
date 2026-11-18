from config import CURA_USERNAME, CURA_PASSWORD


VALID_LOGIN = {
    "username": CURA_USERNAME,
    "password": CURA_PASSWORD,
    "expected": "success"
}

INVALID_USERNAME = {
    "username": "InvalidUser",
    "password": CURA_PASSWORD,
    "expected": "failure"
}

INVALID_PASSWORD = {
    "username": CURA_USERNAME,
    "password": "WrongPassword123",
    "expected": "failure"
}

INVALID_BOTH = {
    "username": "InvalidUser",
    "password": "WrongPassword123",
    "expected": "failure"
}