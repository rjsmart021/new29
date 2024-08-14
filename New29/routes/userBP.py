from flask import Blueprint
from controllers.userController import save, find_all

user_blueprint = Blueprint("user_bp", __name__)

user_blueprint.route('/', methods=['POST'])(save)
user_blueprint.route('/', methods=['GET'])(find_all)