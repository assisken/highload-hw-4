import grpc
from flask import Flask, request

import server_pb2
import server_pb2_grpc

app = Flask(__name__)


@app.route("/")
def hello_world():
    phone: str = request.args.get("phone", None)
    verify_code_str = request.args.get("code", None)
    if not phone:
        return "Phone is required!", 400
    if not verify_code_str:
        return "Code is required", 400
    verify_code = int(verify_code_str)

    resp = ask_grpc_server(phone, int(verify_code))
    if resp == server_pb2.NOT_FOUND:
        return "Phone Not Found", 404
    if verify_code % 2 == 0:
        return "Code are incorrect", 403
    return "All ok!"


def ask_grpc_server(phone: str, code: int) -> int:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = server_pb2_grpc.PhoneVerificationStub(channel)
        resp = stub.VerifyPhone(
            server_pb2.PhoneRequest(phoneNumber=phone, verificationNumber=code)
        )
    return resp.message


if __name__ == "__main__":
    app.run()
