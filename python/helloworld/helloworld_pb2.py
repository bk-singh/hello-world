# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto

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
  name='helloworld.proto',
  package='helloworld',
  syntax='proto3',
  serialized_pb=_b('\n\x10helloworld.proto\x12\nhelloworld\".\n\x0cHelloRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\tJ\x04\x08\x02\x10\x03\"&\n\x06\x64\x65tail\x12\x0e\n\x06status\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x04 \x01(\t\"\xad\x01\n\nHelloReply\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x04 \x01(\t\x12=\n\x0c\x65mplyee_code\x18\x05 \x03(\x0b\x32\'.helloworld.HelloReply.EmplyeeCodeEntry\x1a\x46\n\x10\x45mplyeeCodeEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.helloworld.detail:\x02\x38\x01\"1\n\tHelloList\x12$\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x16.helloworld.HelloReply2\x8d\x01\n\x07Greeter\x12>\n\x08SayHello\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12\x42\n\rSayHelloAgain\x12\x18.helloworld.HelloRequest\x1a\x15.helloworld.HelloList\"\x00\x62\x06proto3')
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='helloworld.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='helloworld.HelloRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='helloworld.HelloRequest.name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=78,
)


_DETAIL = _descriptor.Descriptor(
  name='detail',
  full_name='helloworld.detail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='helloworld.detail.status', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='helloworld.detail.name', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=118,
)


_HELLOREPLY_EMPLYEECODEENTRY = _descriptor.Descriptor(
  name='EmplyeeCodeEntry',
  full_name='helloworld.HelloReply.EmplyeeCodeEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='helloworld.HelloReply.EmplyeeCodeEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='helloworld.HelloReply.EmplyeeCodeEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=294,
)

_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='helloworld.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='helloworld.HelloReply.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='helloworld.HelloReply.name', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emplyee_code', full_name='helloworld.HelloReply.emplyee_code', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HELLOREPLY_EMPLYEECODEENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=294,
)


_HELLOLIST = _descriptor.Descriptor(
  name='HelloList',
  full_name='helloworld.HelloList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='helloworld.HelloList.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=296,
  serialized_end=345,
)

_HELLOREPLY_EMPLYEECODEENTRY.fields_by_name['value'].message_type = _DETAIL
_HELLOREPLY_EMPLYEECODEENTRY.containing_type = _HELLOREPLY
_HELLOREPLY.fields_by_name['emplyee_code'].message_type = _HELLOREPLY_EMPLYEECODEENTRY
_HELLOLIST.fields_by_name['data'].message_type = _HELLOREPLY
DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['detail'] = _DETAIL
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
DESCRIPTOR.message_types_by_name['HelloList'] = _HELLOLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)

detail = _reflection.GeneratedProtocolMessageType('detail', (_message.Message,), dict(
  DESCRIPTOR = _DETAIL,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.detail)
  ))
_sym_db.RegisterMessage(detail)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), dict(

  EmplyeeCodeEntry = _reflection.GeneratedProtocolMessageType('EmplyeeCodeEntry', (_message.Message,), dict(
    DESCRIPTOR = _HELLOREPLY_EMPLYEECODEENTRY,
    __module__ = 'helloworld_pb2'
    # @@protoc_insertion_point(class_scope:helloworld.HelloReply.EmplyeeCodeEntry)
    ))
  ,
  DESCRIPTOR = _HELLOREPLY,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloReply)
  ))
_sym_db.RegisterMessage(HelloReply)
_sym_db.RegisterMessage(HelloReply.EmplyeeCodeEntry)

HelloList = _reflection.GeneratedProtocolMessageType('HelloList', (_message.Message,), dict(
  DESCRIPTOR = _HELLOLIST,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloList)
  ))
_sym_db.RegisterMessage(HelloList)


_HELLOREPLY_EMPLYEECODEENTRY.has_options = True
_HELLOREPLY_EMPLYEECODEENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='helloworld.Greeter',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=348,
  serialized_end=489,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='helloworld.Greeter.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloAgain',
    full_name='helloworld.Greeter.SayHelloAgain',
    index=1,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOLIST,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
