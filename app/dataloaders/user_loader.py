from typing import List
from strawberry.dataloader import DataLoader
from data import db_users

class UserLoader(DataLoader):
    """
    DataLoader for batching and caching user fetches by user ID.
    """
    def __init__(self):
        super().__init__(load_fn=self.batch_load_fn)

    async def batch_load_fn(self, keys: List[int]) -> List[dict]:
        """
        Batch loads users by their IDs.
        Args:
            keys: List of user IDs to fetch.
        Returns:
            List of user dicts corresponding to the given IDs.
        """
        user_map = {user["id"]: user for user in db_users.values()}
        return [user_map.get(key) for key in keys]
