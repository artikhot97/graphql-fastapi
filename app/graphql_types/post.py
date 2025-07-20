import strawberry
from typing import List, Optional
from app.dataloaders.user_loader import UserLoader
from app.dataloaders.tag_loader import TagLoader
from data import db_posts
from app.graphql_types.user import User
from app.graphql_types.tag import Tag
from app.dataloaders.post_loader import PostLoader
from strawberry import Info

@strawberry.type
class Post:
    """
    Represents a social media post with user and tags.
    """
    id: int
    title: str
    content: str
    user_id: int

    @strawberry.field
    async def user(self, info) -> User:
        """
        Returns the user who created the post, using the UserLoader DataLoader for batching.
        """
        return await User.fetch_user_by_id(info, self.user_id) if hasattr(self, 'user_id') else None

    @strawberry.field
    async def tag_objects(self, info) -> List[Tag]:
        """
        Returns the tags associated with this post, using the TagLoader DataLoader for batching.
        """
        print(f"Fetching tags for post ID: {self.id}")
        return await Tag.tags_for_post(info, self.id)
    
    @staticmethod
    async def fetch_posts(info) -> List["Post"]:
        """
        Fetch all posts from the database using the PostLoader DataLoader.
        """
        post_loader = info.context["post_loader"]
        post_ids = [post["id"] for post in db_posts]
        if not post_ids:
            return []
        post_dicts = await post_loader.load_many(post_ids)
        if not post_dicts:
            return []
        return [Post(
            id=post["id"],
            title=post["title"],
            content=post["content"],
            user_id=post["user_id"],
        ) for post in post_dicts if post]

    @staticmethod
    async def fetch_post_by_id(info, post_id: int) -> Optional["Post"]:
        """
        Fetch a single post by its ID using the PostLoader DataLoader.
        """
        loader: PostLoader = info.context["post_loader"]
        post_data = await loader.load(post_id)
        return Post(id=post_data["id"],
                    title=post_data["title"],
                    content=post_data["content"],
                    user_id=post_data["user_id"]) if post_data else None

@strawberry.type
class Query:
    @strawberry.field
    async def get_posts(self, info) -> List[Post]:
        """
        Fetch all posts.
        """
        return await Post.fetch_posts(info)

    @strawberry.field
    async def get_post_detail(self, info, post_id: int) -> Optional[Post]:
        """
        Fetch a single post by its ID.
        """
        return await Post.fetch_post_by_id(info, post_id)
