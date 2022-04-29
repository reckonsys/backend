from functools import wraps

import jwt
from django.conf import settings

from .models import User


def login_required(f):
    @wraps(f)
    def wrapper(root, info, *args, **kwargs):
        # try:
        auth_header = info.context.META.get("HTTP_AUTHORIZATION")
        token = auth_header.split(" ")[1]
        token_json = jwt.decode(
            token,
            settings.KEYCLOAK_PUBLIC_KEY,
            algorithms=["RS256"],
            audience="account",
        )
        try:
            user = User.objects.get(id=token_json["sub"])
        except User.DoesNotExist:
            user = User.objects.create(
                email=token_json["email"],
                id=token_json["sub"],
                first_name=token_json["given_name"],
                last_name=token_json["family_name"],
            )
        info.context.user = user
        # except ExpiredSignatureError:
        return f(root, info, *args, **kwargs)
        # return None

    return wrapper
