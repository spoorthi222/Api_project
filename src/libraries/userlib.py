from django.core.exceptions import ValidationError
from src.models import Users
import binascii,os
import hashlib
SALT_LENGTH = 16
HASH_METHOD = "SHA512"


class UserLib():
    def __init__(self):
        print "Initialized User Lib"

    def validate_signup(self, user_info):

        if "name" not in user_info:
            return ValidationError("Missing Key 'name' ")

        if "email_id" not in user_info:
            return ValidationError("Missing Key 'email_id' ")

        if "password" not in user_info:
            return ValidationError("Missing Key 'password' ")

        users = Users.objects.filter(email_id = user_info["email_id"])
        if users.count() > 0:
           return False

        return True

    def password_hashing(self, password, salt = None):

        if not salt:
            salt = binascii.hexlify(os.urandom(SALT_LENGTH / 2)).decode()

        hash_library = hashlib.new(HASH_METHOD)
        salted_client_hash = str(password + salt)
        hash_library.update(salted_client_hash)
        server_hash = hash_library.hexdigest()
        return (server_hash, salt)

    def createUser(self, user_info):

        validation = self.validate_signup(user_info)
        password_hash, salt = self.password_hashing(password = user_info["password"])
        user_info["password"] = password_hash
        Users.objects.create(**user_info)
        #print Users
        return  "User Created"