import strawberry


from src.graphql.resolvers.resolver import add_shopping_centers
from src.graphql.fragments.fragments import AddShoppingCenterResponse


# Due to lack of time, I wasn't able to create all the CRUD methods, my apologies.
# If you have the opportunity to give me a little more time to work on this project,it would be nice

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def add_shopping_centers(self, name: str) -> AddShoppingCenterResponse:
        """ Add sticky note """
        add_stickynotes_resp = await add_shopping_centers(name)
        return add_stickynotes_resp

