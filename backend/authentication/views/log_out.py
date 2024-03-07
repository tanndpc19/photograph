from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def log_out(request):
    try:
        RefreshToken(str(request.data['token'])).blacklist()

        return Response(data = {"status": "True", "message": "Logged out!"}, status = status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"status": "False", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
