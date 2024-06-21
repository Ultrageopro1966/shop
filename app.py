"""main app."""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

import yaml
from flask import Flask, Response, render_template

from database.database import SupabaseClient
from routes.about_route import AboutRoute
from routes.auth.log_in_route import LogInRoute
from routes.auth.sign_in_route import SignInRoute
from routes.main_route import MainRoute
from routes.secret_route import SecretRoute
from routes.shop.shop_route import ShopRoute
from routes.sponsors_route import SponsorsRoute

# read config
with Path.open("configs.yml") as config_file:
    config = yaml.safe_load(config_file)

SUPABASE_URL = config["supabase"]["project_url"]
SUPABASE_KEY = config["supabase"]["api_key"]
SECRET = config["auth"]["secret"]

# create database client
database = SupabaseClient(SUPABASE_URL, SUPABASE_KEY)

# init app
app = Flask(__name__)


@app.after_request
def add_header(r: Response) -> Response:
    """Add headers to support HTTPS.

    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers["Cache-Control"] = "public, max-age=0"
    return r


about_route = AboutRoute()
main_route = MainRoute()
sign_in_route = SignInRoute(database)
log_in_route = LogInRoute(database)
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
    app.run("0.0.0.0")  # noqa: S104
