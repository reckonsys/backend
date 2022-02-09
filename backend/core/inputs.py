from graphene import ID, Int, String


class IDInput:
    id = ID(required=True)


class CreateUploadInput:
    kind = Int(required=True)
    name = String(required=True)
    mimetype = String(required=True)


class UpdateMeInput:
    first_name = String(required=True)
    last_name = String(required=True)
    email = String(required=True)


class RegisterInput:
    password = String(required=True)
    username = String(required=True)
