"""auth functions."""

from __future__ import annotations

import re

import jwt


def validate_login(login: str) -> bool:
    """Validate login.

    Args:
    ----
    login (str): Логин для валидации.

    Returns:
    -------
    bool: True, если логин соответствует критериям, иначе False.

    """
    min_login_length = 3
    if len(login) <= min_login_length:
        return False
    return True


def validate_password(password: str) -> tuple[str, bool]:
    """Validate password.

    Проверяет пароль на соответствие критериям:
    - Должен быть не менее 8 символов
    - Содержать хотя бы одну заглавную букву
    - Содержать хотя бы одну строчную букву
    - Содержать хотя бы одну цифру
    - Содержать хотя бы один специальный символ (например, !, @, #, $).

    Args:
    ----
    password (str): Строка пароля для валидации.

    Returns:
    -------
    str: Сообщение об ошибке, если пароль не соответствует критериям, иначе "Успех".
    bool: True, если пароль соответствует всем критериям, иначе False.

    """
    min_password_length = 8
    if len(password) < min_password_length:
        return "Пароль должен быть длиной не менее 8 символов.", False
    if not re.search(r"[A-Z]", password):
        return "Пароль должен содержать хотя бы одну заглавную букву.", False
    if not re.search(r"[a-z]", password):
        return "Пароль должен содержать хотя бы одну строчную букву.", False
    if not re.search(r"[0-9]", password):
        return "Пароль должен содержать хотя бы одну цифру.", False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Пароль должен содержать хотя бы один специальный символ.", False
    return "Успех", True


def get_token(login: str, password: str, secret_key: str) -> str:
    """Get token."""
    return jwt.encode({"login": login, "password": password}, secret_key)


def check_password(token: str, real_password: str, secret_key: str) -> bool:
    """Check password."""
    if real_password == jwt.decode(token, secret_key, algorithms=["HS256"])["password"]:
        return True
    return False
