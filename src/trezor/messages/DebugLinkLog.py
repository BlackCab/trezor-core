# Automatically generated by pb2py
import protobuf as p
from micropython import const
t = p.MessageType('DebugLinkLog')
t.wire_type = const(104)
t.add_field(1, 'level', p.UVarintType)
t.add_field(2, 'bucket', p.UnicodeType)
t.add_field(3, 'text', p.UnicodeType)
DebugLinkLog = t
