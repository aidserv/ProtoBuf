# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GenerateRS.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10GenerateRS.proto\x12\x0f\x41ppleRemoteAuth\"\xe0\x01\n\x10RemoteDeviceInfo\x12\x0f\n\x07rq_data\x18\x01 \x01(\x0c\x12\x13\n\x0brq_sig_data\x18\x02 \x01(\x0c\x12\x19\n\x11grappa_session_id\x18\x03 \x01(\r\x12\x1d\n\x15\x66\x61ir_play_certificate\x18\x05 \x01(\x0c\x12\x18\n\x10\x66\x61ir_device_type\x18\x06 \x01(\x03\x12\x16\n\x0e\x66\x61ir_play_guid\x18\x08 \x01(\t\x12\x13\n\x06grappa\x18\t \x01(\x0cH\x00\x88\x01\x01\x12\x11\n\x04\x64sid\x18\n \x01(\x03H\x01\x88\x01\x01\x42\t\n\x07_grappaB\x07\n\x05_dsid\"P\n\x06rsdata\x12\x0f\n\x07rs_data\x18\x01 \x01(\x0c\x12\x0b\n\x03ret\x18\x02 \x01(\x08\x12\x18\n\x0brs_sig_data\x18\x03 \x01(\x0cH\x00\x88\x01\x01\x42\x0e\n\x0c_rs_sig_data\"D\n\x06Grappa\x12\x12\n\ngrappaData\x18\x01 \x01(\x0c\x12\x19\n\x11grappa_session_id\x18\x02 \x01(\r\x12\x0b\n\x03ret\x18\x03 \x01(\x08\"\x1c\n\x0crqGeneGrappa\x12\x0c\n\x04udid\x18\x01 \x01(\t\"f\n\x06scinfo\x12\x0f\n\x07\x61ppleid\x18\x01 \x01(\t\x12\x0c\n\x04\x64sid\x18\x02 \x01(\x03\x12\x0c\n\x04sidb\x18\x03 \x01(\x0c\x12\x0c\n\x04sidd\x18\x04 \x01(\x0c\x12\x0b\n\x03txt\x18\x05 \x01(\x0c\x12\x14\n\x0chardwareInfo\x18\x06 \x01(\x0c\"\x17\n\x08rsscinfo\x12\x0b\n\x03ret\x18\x01 \x01(\x08\x32\xe3\x01\n\x03\x61id\x12J\n\nGenerateRS\x12!.AppleRemoteAuth.RemoteDeviceInfo\x1a\x17.AppleRemoteAuth.rsdata\"\x00\x12J\n\x0eGenerateGrappa\x12\x1d.AppleRemoteAuth.rqGeneGrappa\x1a\x17.AppleRemoteAuth.Grappa\"\x00\x12\x44\n\x0cUploadScinfo\x12\x17.AppleRemoteAuth.scinfo\x1a\x19.AppleRemoteAuth.rsscinfo\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GenerateRS_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REMOTEDEVICEINFO._serialized_start=38
  _REMOTEDEVICEINFO._serialized_end=262
  _RSDATA._serialized_start=264
  _RSDATA._serialized_end=344
  _GRAPPA._serialized_start=346
  _GRAPPA._serialized_end=414
  _RQGENEGRAPPA._serialized_start=416
  _RQGENEGRAPPA._serialized_end=444
  _SCINFO._serialized_start=446
  _SCINFO._serialized_end=548
  _RSSCINFO._serialized_start=550
  _RSSCINFO._serialized_end=573
  _AID._serialized_start=576
  _AID._serialized_end=803
# @@protoc_insertion_point(module_scope)
