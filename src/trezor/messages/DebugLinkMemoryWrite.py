# Automatically generated by pb2py
import protobuf as p
from micropython import const
t = p.MessageType('DebugLinkMemoryWrite')
t.wire_type = const(112)
t.add_field(1, 'address', p.UVarintType)
t.add_field(2, 'memory', p.BytesType)
t.add_field(3, 'flash', p.BoolType)
DebugLinkMemoryWrite = t
