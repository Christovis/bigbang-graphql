from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    graphql_sync, snake_case_fallback_resolvers,
    ObjectType,
)
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from bigbangGraphQL.config import CONFIG
from bigbangGraphQL.api import app, db
from bigbangGraphQL.api.queries import listEmails_resolver, getEmail_resolver
from bigbangGraphQL.api.mutations import (
    create_email_resolver, delete_email_resolver)


query = ObjectType("Query")
query.set_field("getEmail", getEmail_resolver)
query.set_field("listEmails", listEmails_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("createEmail", create_email_resolver)
mutation.set_field("deleteEmail", delete_email_resolver)


@app.route('/')
def hello():
    text = "Welcome to Bigbang's API !!\n" +
           "To connect to the GraphiQL add '/graphql' at the end of the URL"
    return text


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    type_defs = load_schema_from_path(
        CONFIG.folder_proj + "/src/bigbangGraphQL/schema.graphql"
    )
    schema = make_executable_schema(
        type_defs,
        query,
        mutation,
        snake_case_fallback_resolvers,
    )
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
