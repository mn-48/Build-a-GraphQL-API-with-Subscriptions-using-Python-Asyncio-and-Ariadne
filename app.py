from ariadne import (
    load_schema_from_path,
    make_executable_schema, 
    snake_case_fallback_resolvers
)

from ariadne.asgi import GraphQL
from mutations import mutation
from queries import query

type_defs = load_schema_from_path("schema.graphql")

schema = make_executable_schema(
    type_defs, 
    query, 
    mutation,
    snake_case_fallback_resolvers
)

app = GraphQL(schema, debug=True)