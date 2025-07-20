import strawberry
from typing import List, Optional
from data import db_users
from app.dataloaders.user_loader import UserLoader

@strawberry.type
class User:
    """
    A user in the system.
    """
    id: int
    name: str
    description: Optional[str] = None

    @staticmethod
    async def fetch_users(info) -> List["User"]:
        """
        Batch fetch all users using the DataLoader.
        """
        loader: UserLoader = info.context["user_loader"]
        # Batch load all user ids
        user_ids = list(db_users.keys())
        user_dicts = await loader.load_many(user_ids)
        return [User(**user, description=f"User {user['name']}") for user in user_dicts if user]

    @staticmethod
    async def fetch_user_by_id(info, user_id: int) -> Optional["User"]:
        """
        Fetch a single user by id using the DataLoader.
        """
        loader: UserLoader = info.context["user_loader"]
        user = await loader.load(user_id)
        return User(**user, description=f"User {user['name']}") if user else None

@strawberry.type
class Query:
    """
    GraphQL query type for fetching users.
    """
    
    @strawberry.field
    async def fetch_users(self, info) -> List[User]:
        """
        Fetch all users.
        """
        return await User.fetch_users(info)

    @strawberry.field
    async def fetch_user_by_id(self, info, user_id: int) -> Optional[User]:
        """
        Fetch a single user by user_id.
        """
        return await User.fetch_user_by_id(info, user_id)