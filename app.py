"""main app."""

from __future__ import annotations

from uuid import uuid4

from flask import Flask, render_template

from routes.about_route import AboutRoute
from routes.auth.log_in_route import LogInRoute
from routes.auth.sign_in_route import SignInRoute
from routes.main_route import MainRoute
from routes.secret_route import SecretRoute
from routes.shop.shop_route import ShopRoute
from routes.sponsors_route import SponsorsRoute

app = Flask(__name__)

about_route = AboutRoute()
main_route = MainRoute()
sign_in_route = SignInRoute()
log_in_route = LogInRoute()
secret_route = SecretRoute()
sponsors_route = SponsorsRoute()
shop_route = ShopRoute()

app.register_blueprint(about_route.blueprint)
app.register_blueprint(main_route.blueprint)
app.register_blueprint(sign_in_route.blueprint)
app.register_blueprint(log_in_route.blueprint)
app.register_blueprint(secret_route.blueprint)
app.register_blueprint(sponsors_route.blueprint)
app.register_blueprint(shop_route.blueprint)


@app.errorhandler(404)
def page_not_found(_: Exception) -> tuple[str, int]:
    """Handle 404 errors.

    :param _: error
    :return: tuple with render_template and status code
    """
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.secret_key = str(uuid4())
    app.run("0.0.0.0", debug=True)  # noqa: S104
