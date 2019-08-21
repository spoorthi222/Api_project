from django.http import JsonResponse
from rest_framework.views import APIView
from src.libraries.loginlib import LoginLib
from src.api_helper.custom_response import CustomResponse
from rest_framework.status import HTTP_201_CREATED

class LoginView(APIView):

    def post(self, requests):
        user_details = requests.data
        response_text = LoginLib().login(login_detail= user_details)
        return CustomResponse(payload = response_text, code= HTTP_201_CREATED)