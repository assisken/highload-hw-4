require 'grpc'
require_relative 'server_services_pb'

class VerificationService < PhoneVerification::Service
  def verify_phone(request, _unused_call)
    if request.phoneNumber =~ /^7\d{10}/
      return PhoneResponse.new(message: :FOUND)
    end
    PhoneResponse.new(message: :NOT_FOUND)
  end
end

s = GRPC::RpcServer.new
s.add_http2_port('0.0.0.0:50051', :this_port_is_insecure)
s.handle(VerificationService)
s.run_till_terminated_or_interrupted([1, 'int', 'SIGQUIT'])
