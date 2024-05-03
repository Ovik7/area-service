from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException

app = FastAPI(openapi_url="/api/v1/areas/openapi.json", docs_url="/api/v1/areas/docs")

areas_router = APIRouter()

areas = [
    {
        'areas_id': 1,
        'name': 'Binance',
        'description': 'Одна из крупнейших криптовалютных бирж в мире.',
        'count_users': 'Cryptocurrency Exchange',
        'year': '2017'
    },
    {
        'areas_id': 2,
        'name': 'Coinbase',
        'description': 'Одна из наиболее популярных и надежных платформ для обмена криптовалют.',
        'count_users': 'Cryptocurrency Exchange',
        'year': '2012'
    },
    {
        'areas_id': 3,
        'name': 'Kraken',
        'description': 'Один из старейших криптовалютных бирж с широким спектром услуг и высоким уровнем безопасности.',
        'count_users': 'Cryptocurrency Exchange',
        'year': '2011'
    },
    {
        'areas_id': 4,
        'name': 'Bittrex',
        'description': 'Платформа для торговли криптовалютами с широким выбором монет и высокой ликвидностью.',
        'count_users': 'Cryptocurrency Exchange',
        'year': '2014'
    },
    {
        'areas_id': 5,
        'name': 'Huobi',
        'description': 'Мировая криптовалютная биржа с широким спектром услуг и активным сообществом трейдеров.',
        'count_users': 'Cryptocurrency Exchange',
        'year': '2013'
    }
]


@areas_router.get("/")
async def read_areas():
    return areas


@areas_router.get("/{areas_id}")
async def read_area(areas_id: int):
    for area in areas:
        if area['areas_id'] == areas_id:
            return area
    return None


app.include_router(areas_router, prefix='/api/v1/areas', tags=['areas'])

if __name__ == '__main__':
    import uvicorn
    import os

    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
