from typing import List
from strawberry.dataloader import DataLoader
from data import db_posts

class PostLoader(DataLoader):
    """
    DataLoader for batching and caching post fetches by post ID.
    """
    def __init__(self):
        super().__init__(load_fn=self.batch_load_fn)

    async def batch_load_fn(self, keys: List[int]) -> List[dict]:
        """
        Batch loads posts by their IDs.
        Args:
            keys: List of post IDs to fetch.
        Returns:
            List of post dicts corresponding to the given IDs.
        """
        post_map = {post["id"]: post for post in db_posts}
        return [post_map.get(key) for key in keys]
