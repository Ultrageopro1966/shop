from flask import render_template, Blueprint, request


class SecretRoute:
    def __init__(self) -> None:
        self.blueprint = Blueprint("secret", __name__)

        @self.blueprint.route("/secret")
        def secret() -> str:
            return self.__secret()

    def __secret(self) -> str:
        code = request.args.get("code", "0")

        return render_template("secret.html", code=code)
