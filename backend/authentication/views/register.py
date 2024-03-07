from authentication.models import User
from authentication.serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny
 
from django.core.mail import EmailMessage



@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        allData = request.data
        newUserData = {
            'user_name': allData['user_name'],
            'password': allData['password'],
            'password_confirm': allData['password_confirm'],
            'email': allData['email'],
            'type': User.PUBLIC_ACCOUNT,

        }

        userSerializer = UserSerializer(data = newUserData)
        if not userSerializer.is_valid():
            return Response(
                data = {
                    "status": "False",
                    "message": userSerializer.errors
                }, 
                status=status.HTTP_400_BAD_REQUEST)
        
        user = userSerializer.save()
        # message = "hitFSGHDHDAFSGSDFFSDFFSGGSD"
        # email = EmailMessage("Mail confirm registration", message, to=['21020392@vnu.edu.vn'])
        # email.send() 

        data = {
            'status': "True",
            'email': user.email,
            'user_name': user.user_name,
        }
        return Response(data = data, status = status.HTTP_200_OK)

    except Exception as e:
        return Response(data={"status": "False", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
