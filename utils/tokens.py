from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
from userapp.models import UserProfile


def get_user_id_from_token(request):
    try:
        authorization_header = request.headers.get('Authorization')
        if authorization_header:
            access_token = AccessToken(authorization_header.split()[1])
            user_id = access_token['user_id']
            return user_id
        else:
            return
    except (AuthenticationFailed, IndexError):
        return


def get_user(request):
    user_id = get_user_id_from_token(request)
    user = UserProfile.objects.get(id=user_id)
    return user
