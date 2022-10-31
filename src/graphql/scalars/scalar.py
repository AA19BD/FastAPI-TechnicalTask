import strawberry


@strawberry.type
class ShoppingCenter:
    id: int
    name: str


@strawberry.type
class ShoppingCenterExists:
    message: str = "ShoppingCenter with same name exists"


@strawberry.type
class ShoppingCenterNotExists:
    message: str = "ShoppingCenter with same name not exist"


@strawberry.type
class AddShoppingCenter:
    id: int
    name: str
