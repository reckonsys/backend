from graphql_jwt.decorators import login_required, user_passes_test

from .choices import UserKind

login_required = login_required  # Silence Flake8
client_required = user_passes_test(lambda u: u.kind == UserKind.CLIENT)
admin_required = user_passes_test(lambda u: u.kind == UserKind.ADMIN)
