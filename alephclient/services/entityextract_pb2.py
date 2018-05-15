# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alephclient/services/entityextract.proto

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
  name='alephclient/services/entityextract.proto',
  package='alephservices',
  syntax='proto3',
  serialized_pb=_b('\n(alephclient/services/entityextract.proto\x12\ralephservices\"\'\n\x04Text\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x11\n\tlanguages\x18\x02 \x03(\t\"\xb4\x01\n\x0f\x45xtractedEntity\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x0e\n\x06length\x18\x03 \x01(\r\x12\x31\n\x04type\x18\x04 \x01(\x0e\x32#.alephservices.ExtractedEntity.Type\"?\n\x04Type\x12\n\n\x06PERSON\x10\x00\x12\x10\n\x0cORGANIZATION\x10\x01\x12\x0b\n\x07\x43OMPANY\x10\x02\x12\x0c\n\x08LOCATION\x10\x03\x32Q\n\rEntityExtract\x12@\n\x07\x45xtract\x12\x13.alephservices.Text\x1a\x1e.alephservices.ExtractedEntity0\x01\x62\x06proto3')
)



_EXTRACTEDENTITY_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='alephservices.ExtractedEntity.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PERSON', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORGANIZATION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPANY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=218,
  serialized_end=281,
)
_sym_db.RegisterEnumDescriptor(_EXTRACTEDENTITY_TYPE)


_TEXT = _descriptor.Descriptor(
  name='Text',
  full_name='alephservices.Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='alephservices.Text.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='languages', full_name='alephservices.Text.languages', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=59,
  serialized_end=98,
)


_EXTRACTEDENTITY = _descriptor.Descriptor(
  name='ExtractedEntity',
  full_name='alephservices.ExtractedEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='alephservices.ExtractedEntity.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='alephservices.ExtractedEntity.offset', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='alephservices.ExtractedEntity.length', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='alephservices.ExtractedEntity.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXTRACTEDENTITY_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=281,
)

_EXTRACTEDENTITY.fields_by_name['type'].enum_type = _EXTRACTEDENTITY_TYPE
_EXTRACTEDENTITY_TYPE.containing_type = _EXTRACTEDENTITY
DESCRIPTOR.message_types_by_name['Text'] = _TEXT
DESCRIPTOR.message_types_by_name['ExtractedEntity'] = _EXTRACTEDENTITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), dict(
  DESCRIPTOR = _TEXT,
  __module__ = 'alephclient.services.entityextract_pb2'
  # @@protoc_insertion_point(class_scope:alephservices.Text)
  ))
_sym_db.RegisterMessage(Text)

ExtractedEntity = _reflection.GeneratedProtocolMessageType('ExtractedEntity', (_message.Message,), dict(
  DESCRIPTOR = _EXTRACTEDENTITY,
  __module__ = 'alephclient.services.entityextract_pb2'
  # @@protoc_insertion_point(class_scope:alephservices.ExtractedEntity)
  ))
_sym_db.RegisterMessage(ExtractedEntity)



_ENTITYEXTRACT = _descriptor.ServiceDescriptor(
  name='EntityExtract',
  full_name='alephservices.EntityExtract',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=283,
  serialized_end=364,
  methods=[
  _descriptor.MethodDescriptor(
    name='Extract',
    full_name='alephservices.EntityExtract.Extract',
    index=0,
    containing_service=None,
    input_type=_TEXT,
    output_type=_EXTRACTEDENTITY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENTITYEXTRACT)

DESCRIPTOR.services_by_name['EntityExtract'] = _ENTITYEXTRACT

# @@protoc_insertion_point(module_scope)
