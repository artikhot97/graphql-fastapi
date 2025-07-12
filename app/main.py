
import strawberry
from fastapi import FastAPI

from strawberry.fastapi import GraphQLRouter
from graphql_types.books import Query as BookQuery

@strawberry.type
class Query(BookQuery):
    pass


# @strawberry.type
# class Mutation():
#     pass


schema = strawberry.Schema(query=Query) # include mutation=Mutation if you have any
graphql_app: GraphQLRouter = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql",)
