import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.graphql_types.user import Query as UserQuery
from app.graphql_types.post import Query as PostQuery
from app.graphql_types.books import Query as BooksQuery
from app.dataloaders.user_loader import UserLoader
from app.dataloaders.tag_loader import TagLoader
from app.dataloaders.post_loader import PostLoader

@strawberry.type
class Query(PostQuery, UserQuery, BooksQuery):
    pass

async def get_context():
    return {"user_loader": UserLoader(), "tag_loader": TagLoader(), "post_loader": PostLoader()}

schema = strawberry.Schema(query=Query)
graphql_app: GraphQLRouter = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql",)
