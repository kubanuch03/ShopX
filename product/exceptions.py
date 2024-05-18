from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def unauthorized_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if isinstance(exc, AuthenticationFailed):
        return Response({
            "detail": "A user account is not able to create a product."
        }, status=status.HTTP_401_UNAUTHORIZED)
    return response
