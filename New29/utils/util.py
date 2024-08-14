from datetime import datetime, timedelta, timezone
import jwt
import os

# Create a secret key constant variable
SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-passphrase'

def encode_token(user_id):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1),
        'sub': user_id
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token