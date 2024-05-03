from app.api.models import AreaIn

from app.api.db import areas, database


async def add_area(payload: AreaIn):
    query = areas.insert().values(**payload.dict())
    return await database.execute(query=query)


async def areas():
    query = areas.select()
    return await database.fetch_all(query=query)


async def get_area(id):
    query = areas.select(areas.c.id == id)
    return await database.fetch_one(query=query)


async def delete_area(id: int):
    query = areas.delete().where(areas.c.id == id)
    return await database.execute(query=query)


async def update_area(id: int, payload: AreaIn
):
    query = (
        areas
        .update()
        .where(areas.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
