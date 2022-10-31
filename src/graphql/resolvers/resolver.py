from sqlalchemy import delete, select, update, insert
from sqlalchemy.orm import load_only

# from src.graphql.helpers.helper import get_only_selected_fields, get_valid_data
from src.graphql.db.session import get_session
from src.graphql.models import models
from src.graphql.scalars.scalar import (
    ShoppingCenter,
    ShoppingCenterExists,
    AddShoppingCenter,
    ShoppingCenterNotExists
)
# Due to lack of time, I wasn't able to create all the CRUD methods, my apologies.
# If you have the opportunity to give me a little more time to work on this project,it would be nice

async def all_shopping_centers(info):
    async with get_session() as s:
        sql = select(models.ShoppingCenter).order_by(models.ShoppingCenter.name).options(load_only('name'))
        db = (await s.execute(sql)).scalars().unique().all()
    return [i for i in db]


async def shopping_center_name(name: str, info):
    async with get_session() as s:
        sql = select(models.ShoppingCenter).filter(models.ShoppingCenter.name == name).order_by(models.ShoppingCenter.name)
        db = (await s.execute(sql)).scalars().unique().all()
    return [i for i in db]


async def add_shopping_centers(name: str):
    """ Add shopping center """
    async with get_session() as s:
        sql = select(models.ShoppingCenter).options(load_only('name')).filter(models.ShoppingCenter.name == name)
        existing_db_shopping_center = (await s.execute(sql)).first()
        if existing_db_shopping_center is not None:
            return ShoppingCenterExists()

        # db_center = models.ShoppingCenter(name=name)
        # s.add(db_center)
        # await s.commit()

        query = insert(models.ShoppingCenter).values(name=name)
        await s.execute(query)

        sql = select(models.ShoppingCenter).options(load_only('name')).filter(models.ShoppingCenter.name == name)
        db_center = (await s.execute(sql)).scalars().unique().one()
        await s.commit()

        db_center_serialize_data = db_center.as_dict()
    return AddShoppingCenter(**db_center_serialize_data)