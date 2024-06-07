from flask import render_template, Blueprint


class MainRoute:
    def __init__(self) -> None:
        self.blueprint = Blueprint("main", __name__)

        @self.blueprint.route("/")
        def main() -> str:
            return self.__main()

    def __main(self) -> str:
        return render_template("index.html")
