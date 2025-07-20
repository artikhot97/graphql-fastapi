import strawberry
from typing import List
from data import db_tags
from app.dataloaders.tag_loader import TagLoader
from strawberry import Info
@strawberry.type
class Tag:
    """
    Represents a tag that can be associated with posts.
    """

    id: int
    name: str
    post_ids: List[int]
    description: str = ""

    @staticmethod
    async def fetch_tags(info: Info) -> List["Tag"]:
        """
        Returns all tags in the database using the TagLoader DataLoader.
        """
        tag_loader: TagLoader = info.context["tag_loader"]
        tag_ids = [tag["id"] for tag in db_tags]
        result = await tag_loader.load_many(tag_ids)
        return [Tag(id=tag["id"],
                    name=tag["name"],
                    post_ids=tag["post_ids"],
                    description=f"Tag for {tag['name']}") for tag in result if tag]

    @staticmethod
    async def tags_for_post(info: Info, post_id: int) -> List["Tag"]:
        """
        Returns all tags associated with a given post ID using the TagLoader DataLoader.
        """
        tag_loader: TagLoader = info.context["tag_loader"]
        tag_ids = [tag["id"] for tag in db_tags if post_id in tag["post_ids"]]
        result = await tag_loader.load_many(tag_ids)

        return [ Tag(id=tag["id"],
                      name=tag["name"],
                        post_ids=tag["post_ids"],
                      description=f"Tag for {tag['name']}") for tag in result if tag ]