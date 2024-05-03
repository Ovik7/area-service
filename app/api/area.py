from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import AreaOut, AreaIn, AreaUpdate
from app.api import db_manager
from app.api.service import is_label_present

area = APIRouter()

@area.post('/', response_model=AreaIn, status_code=201)
async def create_area(payload: AreaIn):
    for label_id in payload.labels_id:
        if not is_label_present(label_id):
            raise HTTPException(status_code=404, detail=f"Label with given id:{label_id} not found")

    area_id = await db_manager.add_area(payload)
    response = {
        'id': area_id,
        **payload.dict()
    }

    return response

@area.get('/', response_model=List[AreaOut])
async def get_areas():
    return await db_manager.get_all_areas()

@area.get('/{id}/', response_model=AreaOut)
async def get_area(id: int):
    area = await db_manager.get_area(id)
    if not area:
        raise HTTPException(status_code=404, detail="area not found")
    return area

@area.put('/{id}/', response_model=AreaOut)
async def update_area(id: int, payload: AreaUpdate):
    area = await db_manager.get_area(id)
    if not area:
        raise HTTPException(status_code=404, detail="Label not found")

    update_data = payload.dict(exclude_unset=True)

    if 'labels_id' in update_data:
        for label_id in payload.labels_id:
            if not is_label_present(label_id):
                raise HTTPException(status_code=404, detail=f"Label with given id:{label_id} not found")

    area_in_db = AreaIn(**area)

    updated_area = area_in_db.copy(update=update_data)

    return await db_manager.update_area(id, updated_area)

@area.delete('/{id}/', response_model=None)
async def delete_area(id: int):
    area = await db_manager.get_area(id)
    if not area:
        raise HTTPException(status_code=404, detail="area not found")
    return await db_manager.delete_area(id)