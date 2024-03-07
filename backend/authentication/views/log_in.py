from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth.hashers import check_password

from ..token import create_access_token, create_refresh_token
from rest_framework_simplejwt.tokens import RefreshToken


from ..models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def log_in(resquest):
    try:
        user_data = resquest.data
        # check userName
        user = User.objects.filter(userName = user_data['userName']).first()
        if user is None:
            return Response(data={"status": "False", "message": "Username does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        # check password
        if not check_password(user_data['password'], user.password):
            return Response(data={"status": "False", "message": "Wrong password"}, status=status.HTTP_401_UNAUTHORIZED)
        print(type(user))
        # gen token
        refresh_token = RefreshToken.for_user(user)
        data = {
            "access_token": str(refresh_token.access_token),
            "user": {
                "id": user.id,
                "userName": user.userName,
                "email": user.email
            }
        }
        return Response(data = data, status = status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"status": "False", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([AllowAny])
def log_out(request):
    response = Response()
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    response.data = {
        'status': "True",
        'message': "Success"
    }
    response.status_code = status.HTTP_200_OK
    return response