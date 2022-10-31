import strawberry


from src.graphql.scalars.scalar import (
    ShoppingCenter,
    ShoppingCenterExists,
    AddShoppingCenter,
    ShoppingCenterNotExists
)


AddShoppingCenterResponse = strawberry.union(
    "AddShoppingCenterResponse",(ShoppingCenter, ShoppingCenterExists, AddShoppingCenter, ShoppingCenterNotExists),
)
