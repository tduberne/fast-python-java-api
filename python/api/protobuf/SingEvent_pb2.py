# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SingEvent.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SingEvent.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0fSingEvent.proto\"\x94\x01\n\tSingEvent\x12\x0f\n\x07\x61gentId\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\x01\x12\x1d\n\x04song\x18\x03 \x01(\x0e\x32\x0f.SingEvent.Song\"I\n\x04Song\x12\x12\n\x0eOLD_MC_DONALDS\x10\x00\x12\x14\n\x10IF_YOU_ARE_HAPPY\x10\x01\x12\x17\n\x13NINETY_NINE_BOTTLES\x10\x02\x42/\n-ch.dubernet.demopythonapi.simulation.protobufb\x06proto3')
)



_SINGEVENT_SONG = _descriptor.EnumDescriptor(
  name='Song',
  full_name='SingEvent.Song',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OLD_MC_DONALDS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IF_YOU_ARE_HAPPY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NINETY_NINE_BOTTLES', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=95,
  serialized_end=168,
)
_sym_db.RegisterEnumDescriptor(_SINGEVENT_SONG)


_SINGEVENT = _descriptor.Descriptor(
  name='SingEvent',
  full_name='SingEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentId', full_name='SingEvent.agentId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='SingEvent.time', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='song', full_name='SingEvent.song', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SINGEVENT_SONG,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=168,
)

_SINGEVENT.fields_by_name['song'].enum_type = _SINGEVENT_SONG
_SINGEVENT_SONG.containing_type = _SINGEVENT
DESCRIPTOR.message_types_by_name['SingEvent'] = _SINGEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SingEvent = _reflection.GeneratedProtocolMessageType('SingEvent', (_message.Message,), dict(
  DESCRIPTOR = _SINGEVENT,
  __module__ = 'SingEvent_pb2'
  # @@protoc_insertion_point(class_scope:SingEvent)
  ))
_sym_db.RegisterMessage(SingEvent)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n-ch.dubernet.demopythonapi.simulation.protobuf'))
# @@protoc_insertion_point(module_scope)
