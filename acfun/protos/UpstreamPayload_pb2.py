# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UpstreamPayload.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import UserInstance_pb2 as UserInstance__pb2
import SettingInfo_pb2 as SettingInfo__pb2
import RequestBasicInfo_pb2 as RequestBasicInfo__pb2
import FrontendInfo_pb2 as FrontendInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15UpstreamPayload.proto\x12\nAcFunDanmu\x1a\x12UserInstance.proto\x1a\x11SettingInfo.proto\x1a\x16RequestBasicInfo.proto\x1a\x12\x46rontendInfo.proto\"\xe8\x02\n\x0fUpstreamPayload\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\x12\r\n\x05seqId\x18\x02 \x01(\x03\x12\x12\n\nretryCount\x18\x03 \x01(\r\x12\x13\n\x0bpayloadData\x18\x04 \x01(\x0c\x12.\n\x0cuserInstance\x18\x05 \x01(\x0b\x32\x18.AcFunDanmu.UserInstance\x12\x11\n\terrorCode\x18\x06 \x01(\x05\x12,\n\x0bsettingInfo\x18\x07 \x01(\x0b\x32\x17.AcFunDanmu.SettingInfo\x12\x36\n\x10requestBasicInfo\x18\x08 \x01(\x0b\x32\x1c.AcFunDanmu.RequestBasicInfo\x12\x0e\n\x06subBiz\x18\t \x01(\t\x12.\n\x0c\x66rontendInfo\x18\n \x01(\x0b\x32\x18.AcFunDanmu.FrontendInfo\x12\x0b\n\x03kpn\x18\x0b \x01(\t\x12\x16\n\x0e\x61nonymouseUser\x18\x0c \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'UpstreamPayload_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _UPSTREAMPAYLOAD._serialized_start=121
  _UPSTREAMPAYLOAD._serialized_end=481
# @@protoc_insertion_point(module_scope)
