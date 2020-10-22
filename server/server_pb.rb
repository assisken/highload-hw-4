# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto

require 'google/protobuf'

Google::Protobuf::DescriptorPool.generated_pool.build do
  add_file("server.proto", :syntax => :proto3) do
    add_message "PhoneRequest" do
      optional :phoneNumber, :string, 1
    end
    add_message "PhoneResponse" do
      optional :message, :enum, 1, "Response"
    end
    add_enum "Response" do
      value :FOUND, 0
      value :NOT_FOUND, 1
    end
  end
end

PhoneRequest = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("PhoneRequest").msgclass
PhoneResponse = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("PhoneResponse").msgclass
Response = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("Response").enummodule
