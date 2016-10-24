# Automatically generated by pb2py
import protobuf as p
from micropython import const
from .IdentityType import IdentityType
t = p.MessageType('SignIdentity')
t.wire_type = const(53)
t.add_field(1, 'identity', p.EmbeddedMessage(IdentityType))
t.add_field(2, 'challenge_hidden', p.BytesType)
t.add_field(3, 'challenge_visual', p.UnicodeType)
t.add_field(4, 'ecdsa_curve_name', p.UnicodeType)
SignIdentity = t
