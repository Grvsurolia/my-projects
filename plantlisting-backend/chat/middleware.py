from urllib.parse import parse_qs

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from channels.auth import AuthMiddleware, AuthMiddlewareStack, UserLazyObject
from channels.db import database_sync_to_async
from channels.sessions import CookieMiddleware, SessionMiddleware
# from rest_framework_simplejwt.tokens import AccessToken
from CustomUserModel.models import CustomUser
import jwt
from rest_framework_simplejwt.backends import TokenBackend

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


# User = get_user_model()

"""[summary]
plucks the JWT access token from the query string and retrieves the associated user.
  Once the WebSocket connection is opened, all messages can be sent and received without
  verifying the user again. Closing the connection and opening it again 
  requires re-authorization.
for example: 
ws://localhost:8000/<route>/?token=<token_of_the_user>

"""

import base64
import json
@database_sync_to_async
def get_user(scope):
    close_old_connections()
    query_string = parse_qs(scope['query_string'].decode())
    token = query_string.get('token')

    if not token:
        return AnonymousUser()
    try:
        data = {'token':token[0]}
        
        valid_data = TokenBackend(algorithm='HS256').decode(token[0],verify=False)
        user = CustomUser.objects.get(id=valid_data['user_id'])
        
    except Exception as exception:
        return AnonymousUser()
    if not user.is_active:
        return AnonymousUser()
    return user


class TokenAuthMiddleware(AuthMiddleware):
    async def resolve_scope(self, scope):
        scope['user']._wrapped = await get_user(scope)


def TokenAuthMiddlewareStack(inner):
    return CookieMiddleware(SessionMiddleware(TokenAuthMiddleware(inner)))
