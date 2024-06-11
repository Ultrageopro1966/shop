"""sign in route."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flask import Blueprint, render_template, request

if TYPE_CHECKING:
    from werkzeug.wrappers.response import Response

    from database.database import SupabaseClient


class LogInRoute:
    """Login route class."""

    def __init__(self: LogInRoute, database: SupabaseClient) -> None:
        """Init login route."""
        self.blueprint = Blueprint("log-in", __name__)
        self.database = database

        @self.blueprint.route("/login", methods=["GET", "POST"])
        def signin() -> tuple[str | Response, int]:
            return self.__signin()

    def __signin(self: LogInRoute) -> tuple[str | Response, int]:
        """Login."""
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]

            response_text, response_code = self.authenticate(email, password)
            if not response_code:
                return (
                    render_template(
                        "log_in.html",
                        error=response_text,
                    ),
                    403,
                )

            # Redirect to a different page if login is successful
            return render_template("log_in.html", success=response_text), 200
        return render_template("log_in.html"), 200

    def authenticate(
        self: LogInRoute,
        login: str,
        password: str,
    ) -> tuple[str, bool]:
        """Auth func logic."""
        user = self.database.get_user(login)

        if user is None:
            return "Зарегестрируйся, пидрила", False

        if user["password"] != password:
            return "Неверный пароль, пидарас", False

        return "Молодчинка! Ты вошел и готов фармить джарахова!!!", True
