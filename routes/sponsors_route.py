from flask import render_template, Blueprint


class SponsorsRoute:
    def __init__(self) -> None:
        self.blueprint = Blueprint("sponsors", __name__)

        @self.blueprint.route("/sponsors")
        def sponsors() -> str:
            return self.__sponsors()

    def __sponsors(self) -> str:
        return render_template("sponsors.html")
