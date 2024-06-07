from flask import render_template, Blueprint


class AboutRoute:
    def __init__(self) -> None:
        self.blueprint = Blueprint("about", __name__)

        @self.blueprint.route("/about")
        def about() -> str:
            return self.__about()

    def __about(self) -> str:
        return render_template("about.html")
