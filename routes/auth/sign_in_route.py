"""sign in route."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flask import Blueprint, redirect, render_template, request

if TYPE_CHECKING:
    from werkzeug.wrappers.response import Response


class SignInRoute:
    """Sign in route class."""

    def __init__(self: SignInRoute) -> None:
        """Init sign in route."""
        self.blueprint = Blueprint("sign-in", __name__)

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
            if not self.authenticate(email, password):
                return (
                    render_template(
                        "sign_in.html", error="Регистрация еще не сделана. Пошел нахуй."
                    ),
                    501,
                )

            # Redirect to a different page if login is successful
            return redirect("/shop"), 200
        return render_template("sign_in.html"), 200

    def authenticate(
        self: SignInRoute,
        email: str | None,
        password: str | None,
    ) -> bool:
        """Auth func logic."""
        return False
