from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_event():
    return "event app created!"
