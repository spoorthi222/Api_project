from rest_framework.views import APIView
from src.api_helper.custom_response import CustomResponse
from rest_framework.status import HTTP_200_OK
from src.api_helper.custom_permission import IsAuthenticated

class AuthView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, requests):
        print requests.GET
        return CustomResponse(payload="Success", code=HTTP_200_OK)
