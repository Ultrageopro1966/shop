"""sign in route."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flask import Blueprint, render_template, request

from modules.auth import validate_login, validate_password

if TYPE_CHECKING:
    from werkzeug.wrappers.response import Response

    from database.database import SupabaseClient


class SignInRoute:
    """Sign in route class."""

    def __init__(self: SignInRoute, database: SupabaseClient) -> None:
        """Init sign in route."""
        self.blueprint = Blueprint("sign-in", __name__)
        self.database = database

        @self.blueprint.route("/sign-in", methods=["GET", "POST"])
        def signin() -> tuple[str | Response, int]:
            return self.__signin()

    def __signin(self: SignInRoute) -> tuple[str | Response, int]:
        """Sign in."""
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get(
                "password",
            )  # Here, add your authentication logic and user check

            if email is None or password is None:
                return render_template("sign_in.html", error="Заполните все поля."), 501

            res, msg = self.authenticate(email, password)
            if not res:
                return (
                    render_template(
                        "sign_in.html",
                        error=f"{msg} Пошел нахуй.",
                    ),
                    403,
                )

            # Redirect to a different page if login is successful
            return (
                render_template(
                    "sign_in.html",
                    success="Молодчинка! Теперь ты в залупе!",
                ),
                200,
            )
        return render_template("sign_in.html"), 200

    def authenticate(
        self: SignInRoute,
        login: str,
        password: str,
    ) -> tuple[bool, str]:
        """Auth func logic."""
        pswr_val_msg, pwrd_val = validate_password(password)
        login_val = validate_login(login)

        # Login validation
        if not login_val:
            return False, "Логин не прошел валидацию. Пошел нахуй."

        # Password validation
        if not pwrd_val:
            return False, pswr_val_msg

        result = self.database.new_user(login, password)
        if not result:
            return False, "Произошла ошибка при создании пользователя. Пошел нахуй."

        return True, "Успех."
