from flask import render_template, Blueprint

class SignUpRoute:
    def __init__(self) -> None:
        self.blueprint = Blueprint('sign-up', __name__)

        @self.blueprint.route('/sign-up')
        def signup():
            return self.__signup()
        
    def __signup(self):
        return render_template('501.html'), 501