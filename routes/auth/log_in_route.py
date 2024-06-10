"""sign in route."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flask import Blueprint, redirect, render_template, request

if TYPE_CHECKING:
    from werkzeug.wrappers.response import Response


class LogInRoute:
    """Login route class."""

    def __init__(self: LogInRoute) -> None:
        """Init login route."""
        self.blueprint = Blueprint("log-in", __name__)

        @self.blueprint.route("/login", methods=["GET", "POST"])
        def signin() -> tuple[str | Response, int]:
            return self.__signin()

    def __signin(self: LogInRoute) -> tuple[str | Response, int]:
        """Login."""
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get(
                "password",
            )  # Here, add your authentication logic and user check
            if not self.authenticate(email, password):
                return (
                    render_template(
                        "sign_in.html", error="Логин еще не сделан. Пошел нахуй."
                    ),
                    501,
                )

            # Redirect to a different page if login is successful
            return redirect("/shop"), 200
        return render_template("log_in.html"), 200

    def authenticate(
        self: LogInRoute,
        email: str | None,
        password: str | None,
    ) -> bool:
        """Auth func logic."""
        return False
