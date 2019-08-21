from django.http import JsonResponse
from rest_framework.views import APIView
from src.libraries.userlib import UserLib
from src.api_helper.custom_response import CustomResponse
from rest_framework.status import HTTP_201_CREATED

class UserView(APIView):

    def post(self, requests):
        print "success1"
        user_details = requests.data
        print "success 2"
        response_text = UserLib().createUser(user_info= user_details)
        return CustomResponse(payload = response_text, code= HTTP_201_CREATED)