from flask import Flask
from database import db
from schemas import ma
from limiter import limiter
from caching import cache

from models.user import User

from routes.customerBP import customer_blueprint
from routes.employeeBP import employee_blueprint
from routes.orderBP import order_blueprint
from routes.productBP import product_blueprint
from routes.productionBP import production_blueprint
from routes.userBP import user_blueprint
from routes.loginBP import login_blueprint


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    blueprint_config(app)
    config_rate_limit()
    
    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(employee_blueprint, url_prefix='/employees')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(production_blueprint, url_prefix='/productions')
    app.register_blueprint(user_blueprint, url_prefix='/users')
    app.register_blueprint(login_blueprint, url_prefix='/login')

def config_rate_limit():
    limiter.limit("6 per minute")(customer_blueprint)
    limiter.limit("10 per hour")(employee_blueprint)
    limiter.limit("1 per second")(order_blueprint)
    limiter.limit("10 per minute")(product_blueprint)
    limiter.limit("20 per hour")(production_blueprint)

if __name__ == "__main__":
    app = create_app('DevelopmentConfig')

    
    
    # with app.app_context():
    #     db.drop_all()
        # db.create_all()
        
    app.run(debug=True)