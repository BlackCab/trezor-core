# Automatically generated by pb2py
import protobuf as p
from micropython import const
t = p.MessageType('EthereumTxAck')
t.wire_type = const(60)
t.add_field(1, 'data_chunk', p.BytesType)
EthereumTxAck = t
