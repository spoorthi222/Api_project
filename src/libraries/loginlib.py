from src.models import Users, Token
import binascii, os, hashlib
from django.core.exceptions import ValidationError

SALT_LENGTH = 16
HASH_METHOD = "SHA512"

class LoginLib():
    def __init__(self):
        print "Login lib is working "

    def password_hashing(self, password, salt= None):
        if not salt:
            salt = binascii.hexlify(os.urandom(SALT_LENGTH / 2)).decode()

        hash_library = hashlib.new(HASH_METHOD)
        salted_client_hash = str(password + salt)
        hash_library.update(salted_client_hash)
        server_hash = hash_library.hexdigest()
        return (server_hash, salt)

    def validateLogin(self, login_detail):
        if "email_id" not in login_detail:
            raise ValidationError("email_id not found")

        if "password" not in login_detail:
            raise ValidationError("password not found")

        users = Users.objects.filter(email_id = login_detail["email_id"])
        if (users.count() > 0):
            selected_user = users[0]

            password_from_db = selected_user.password
            salt_from_db = selected_user.salt

            password_hash_req, salt = self.password_hashing(
                password= login_detail["password"], salt=salt_from_db
            )

            if (password_from_db == password_hash_req):
                self.user_selected = selected_user
                return True
            else:
                raise ValidationError("Invalid Password")
        raise ValidationError("User Not Found")

    def login(self, login_detail):

        user = self.validateLogin(login_detail)
        validation = self.validateLogin(login_detail)
        if(validation):
            token, created = Token.objects.get_or_create(user = self.user_selected)
            response = {"token": token.access_token}
            return response
        return "Login Successful"