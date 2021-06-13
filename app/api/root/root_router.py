from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

root_router = APIRouter()


@root_router.get("/")
async def get_root():
    json_compatible_item_data = jsonable_encoder({'status_code': 200, 'message': 'OK'})
    return JSONResponse(content=json_compatible_item_data)
