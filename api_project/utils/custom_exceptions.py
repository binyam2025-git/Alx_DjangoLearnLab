# Alx_DjangoLearnLab/api_project/utils/custom_exceptions.py
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, AuthenticationFailed, PermissionDenied, NotAuthenticated

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        # You can log the error if needed
        # import logging
        # logger = logging.getLogger(__name__)
        # logger.error(f"API Error: {exc} - Details: {response.data}")

        # Example: Customize ValidationError response
        if isinstance(exc, ValidationError):
            custom_response_data = {
                'status': 'error',
                'code': 'validation_error',
                'message': 'Input validation failed.',
                'errors': response.data # Keep original detailed errors
            }
            response.data = custom_response_data
            response.status_code = status.HTTP_400_BAD_REQUEST # Ensure correct status code

        # Example: Customize Authentication/Permission errors
        elif isinstance(exc, (AuthenticationFailed, NotAuthenticated, PermissionDenied)):
            custom_response_data = {
                'status': 'error',
                'code': 'authentication_or_permission_error',
                'message': 'Authentication or permission denied.',
                'detail': response.data.get('detail', 'You do not have permission to perform this action.')
            }
            response.data = custom_response_data
            response.status_code = response.status_code # Keep original status code (401/403)

        # You can add more elif conditions for other exception types (e.g., Http404, etc.)
        # For unhandled exceptions, you might want a generic error message
        else:
            if response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
                response.data = {
                    'status': 'error',
                    'code': 'internal_server_error',
                    'message': 'An unexpected error occurred. Please try again later.'
                }
    return response