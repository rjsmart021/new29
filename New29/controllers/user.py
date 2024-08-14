from flask import request, jsonify
from schemas.userSchema import user_input_schema, user_output_schema, user_login_schema, users_schema
from services import userService
from marshmallow import ValidationError

# save new user to table
def save():
    try:
        # Validate and deserialize the request data
        user_data = user_input_schema.load(request.json)
        user_save = userService.save(user_data)
        return user_output_schema.jsonify(user_save), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except ValueError as err:
        return jsonify({"error": str(err)}), 400

def find_all():
    users = userService.find_all()
    return users_schema.jsonify(users), 200

# attempt login and return token on success
def login():
    try:
        user_data = user_login_schema.load(request.json)
        token = userService.login(user_data['username'], user_data['password'])
        if token:
            resp = {
                "status": "success",
                "message": "You have successfully logged in",
                "token": token
            }
            return jsonify(resp), 200
        else:
            resp = {
                "status": "error",
                "message": "Username and/or password is incorrect"
            }
            return jsonify(resp), 401
    except ValidationError as err:
        return jsonify(err.messages), 400
    