from ariadne.asgi import GraphQL
from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    QueryType,
    snake_case_fallback_resolvers
)
from resolvers import resolve_contract

query = QueryType()

# Bind resolver
query.set_field("contract", resolve_contract)

# load schema
type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query, snake_case_fallback_resolvers)


app = GraphQL(schema, debug=True)