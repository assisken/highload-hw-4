# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: server.proto for package ''

require 'grpc'
require_relative 'server_pb'

module PhoneVerification
  class Service

    include GRPC::GenericService

    self.marshal_class_method = :encode
    self.unmarshal_class_method = :decode
    self.service_name = 'PhoneVerification'

    rpc :VerifyPhone, ::PhoneRequest, ::PhoneResponse
  end

  Stub = Service.rpc_stub_class
end