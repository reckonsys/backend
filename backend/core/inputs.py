from graphene import ID, Int, String


class IDInput:
    id = ID(required=True)


class CreateUploadInput:
    kind = Int(required=True)
    name = String(required=True)
    mimetype = String(required=True)
