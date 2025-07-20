from typing import List
from strawberry.dataloader import DataLoader
from data import db_tags

class TagLoader(DataLoader):
    """
    DataLoader for batching and caching tag fetches by tag ID.
    """
    def __init__(self):
        super().__init__(load_fn=self.batch_load_fn)

    async def batch_load_fn(self, keys: List[int]) -> List[dict]:
        """
        Batch loads tags by their IDs.
        Args:
            keys: List of tag IDs to fetch.
        Returns:
            List of tag dicts corresponding to the given IDs.
        """
        tag_map = {tag["id"]: tag for tag in db_tags}
        return [tag_map.get(key) for key in keys]
