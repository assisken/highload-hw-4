import grpc

import server_pb2
import server_pb2_grpc


def ask_grpc_server(phone: str) -> int:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = server_pb2_grpc.PhoneVerificationStub(channel)
        resp = stub.VerifyPhone(server_pb2.PhoneRequest(phoneNumber=phone))
    return resp.message
