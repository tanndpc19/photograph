from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(['GET'])
@permission_classes([AllowAny])
def testAuth(request):
    try:
        data = {
            'message': 'abc'
        }
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"status": "False", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
