# Automatically generated by pb2py
import protobuf as p


class SelfTest(p.MessageType):
    MESSAGE_WIRE_TYPE = 32
    FIELDS = {
        1: ('payload', p.BytesType, 0),
    }

    def __init__(
        self,
        payload: bytes = None
    ) -> None:
        self.payload = payload
