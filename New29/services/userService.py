from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from utils.util import encode_token

def save(user_data):
    with Session(db.engine) as session:
        with session.begin():
            # check to see if any user has passed in username
            user_query = select(User).where(User.username == user_data['username'])
            user_check = db.session.execute(user_query).scalars().first()
            if user_check:
                raise ValueError("User with that username already exists")
            
            # create a new instance of User
            new_user = User(
                username=user_data['username'], 
                password=generate_password_hash(user_data['password']),
                role=user_data['role'])
            session.add(new_user)
            session.commit()
        session.refresh(new_user)
        return new_user

# Get all users in database
def find_all():
    query = db.select(User)
    users = db.session.execute(query).scalars().all()
    return users

# function will return token if login is successful
def login(username, password):
    # Query the user table for specified username
    query = db.select(User).where(User.username == username)
    user = db.session.execute(query).scalars().first()
    if user is not None and check_password_hash(user.password, password):
        # Create a token with the user's id
        auth_token = encode_token(user.id)
        return auth_token
    else:
        return None