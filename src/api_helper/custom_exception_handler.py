from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from src.api_helper.custom_response import CustomResponse

def custom_handler(excpetion_object,context):

    message = excpetion_object.message

    if excpetion_object.__class__.__name__ == "ValidationError":
        code = HTTP_400_BAD_REQUEST
    elif excpetion_object.__class__.__name__ == "KeyError":
        code = HTTP_400_BAD_REQUEST
    else :
        code = HTTP_500_INTERNAL_SERVER_ERROR

    response = CustomResponse(
        payload= None, code= code, message = message, status = False
    )
    return response