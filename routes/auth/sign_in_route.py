from flask import render_template, Blueprint

class SignInRoute:
    def __init__(self) -> None:
        self.blueprint = Blueprint('sign-in', __name__)

        @self.blueprint.route('/sign-in')
        def signin():
            return self.__signin()
        
    def __signin(self):
        return render_template('501.html'), 501