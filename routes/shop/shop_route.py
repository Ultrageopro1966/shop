from flask import render_template, Blueprint

class ShopRoute:
    def __init__(self) -> None:
        self.blueprint = Blueprint('shop', __name__)

        @self.blueprint.route('/shop')
        def shop():
            return self.__shop()
        
    def __shop(self):
        return render_template('501.html'), 501