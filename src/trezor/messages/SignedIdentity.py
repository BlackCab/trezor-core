# Automatically generated by pb2py
import protobuf as p


class SignedIdentity(p.MessageType):
    MESSAGE_WIRE_TYPE = 54
    FIELDS = {
        1: ('address', p.UnicodeType, 0),
        2: ('public_key', p.BytesType, 0),
        3: ('signature', p.BytesType, 0),
    }

    def __init__(
        self,
        address: str = None,
        public_key: bytes = None,
        signature: bytes = None
    ) -> None:
        self.address = address
        self.public_key = public_key
        self.signature = signature
