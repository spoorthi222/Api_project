from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

class CustomResponse(Response):
    def __init__(self, message="Learner Bee API", payload= None, code= HTTP_200_OK, status= True):

        data = {
            "status" : status,
            "payload": payload,
            "message": message
        }
        super(CustomResponse, self).__init__(data = data, status = code)