import time
import random
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import mask_hash, check_password
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def safe_check_password(password, encoded):
    if not encoded or encoded.startswith("!"):
        mask_hash(password)
        time.sleep(0.4)
        return False
    return check_password(password, encoded)

class SafeModelBackend(ModelBackend):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None
        
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            mask_hash(password)
            time.sleep(0.4)
            return None

        if safe_check_password(password, user.password):
            return user
        return None