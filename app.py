from flask import Flask, request
from flask_graphql import GraphQLView

import server_pb2
from ask_grpc import ask_grpc_server
from schema import schema

app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))


@app.route("/")
def hello_world():
    phone: str = request.args.get("phone", None)
    verify_code_str = request.args.get("code", None)
    if not phone:
        return "Phone is required!", 400
    if not verify_code_str:
        return "Code is required", 400
    verify_code = int(verify_code_str)

    resp = ask_grpc_server(phone)
    if resp == server_pb2.NOT_FOUND:
        return "Phone Not Found", 404
    if verify_code % 2 == 0:
        return "Code are incorrect", 403
    return "All ok!"


if __name__ == "__main__":
    app.run()
