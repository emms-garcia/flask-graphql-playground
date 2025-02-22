from ariadne import graphql_sync
from ariadne.explorer import ExplorerGraphiQL
from flask import Blueprint, current_app, jsonify, request

from api.schema import schema


blueprint = Blueprint("main", __name__)
html = ExplorerGraphiQL().html(None)

@blueprint.get("/ping")
def ping():
    return "pong", 200


@blueprint.get("/graphql")
def graphql_playground():
    return html, 200


@blueprint.post("/graphql")
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=current_app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
