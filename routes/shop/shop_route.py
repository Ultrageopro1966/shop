"""shop route."""

from __future__ import annotations

from flask import Blueprint, render_template


class ShopRoute:
    """Shop route class."""

    def __init__(self: ShopRoute) -> None:
        """Init shop route."""
        self.blueprint = Blueprint("shop", __name__)

        @self.blueprint.route("/shop")
        def shop() -> tuple[str, int]:
            return self.__shop()

    def __shop(self: ShopRoute) -> tuple[str, int]:
        return render_template("shop.html"), 200
