import strawberry
from pydantic import typing
from strawberry.types import Info

from src.graphql.resolvers.resolver import all_shopping_centers, shopping_center_name
from src.graphql.scalars.scalar import ShoppingCenter
from ..fragments.fragments import AddShoppingCenterResponse

# Due to lack of time, I wasn't able to create all the CRUD methods, my apologies.
# If you have the opportunity to give me a little more time to work on this project,it would be nice


@strawberry.type
class Query:
    @strawberry.field
    async def shopping_centers(self, info: Info) -> typing.List[ShoppingCenter]:
        """Get all shopping centers"""
        shopping_centers_list = await all_shopping_centers(info)
        return shopping_centers_list

    @strawberry.field
    async def shopping_center(self, info: Info, name: str) -> typing.List[ShoppingCenter]:
        """ Get specific shopping center by name """
        users_data_list = await shopping_center_name(name, info)
        return users_data_list

