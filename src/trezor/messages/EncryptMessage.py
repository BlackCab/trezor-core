# Automatically generated by pb2py
import protobuf as p
if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None


class EncryptMessage(p.MessageType):
    MESSAGE_WIRE_TYPE = 49
    FIELDS = {
        1: ('pubkey', p.BytesType, 0),
        2: ('message', p.BytesType, 0),
        3: ('display_only', p.BoolType, 0),
        4: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        5: ('coin_name', p.UnicodeType, 0),  # default='Bitcoin'
    }

    def __init__(
        self,
        pubkey: bytes = None,
        message: bytes = None,
        display_only: bool = None,
        address_n: List[int] = None,
        coin_name: str = None
    ) -> None:
        self.pubkey = pubkey
        self.message = message
        self.display_only = display_only
        self.address_n = address_n if address_n is not None else []
        self.coin_name = coin_name
