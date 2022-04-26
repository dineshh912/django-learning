from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken
from .serializers import UserValidateSerializer



User = get_user_model()

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def micrologin(request):
    serializer = UserValidateSerializer(data=request.data)
    user = serializer.decode_and_authorize(request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)        
    
    # user = serializer.save()
    print(serializer)
    refresh = RefreshToken.for_user(user)
    res = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)