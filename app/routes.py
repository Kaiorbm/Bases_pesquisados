from fastapi import APIRouter, HTTPException
from .models import IDRequest
from .utils import id_exists

router = APIRouter()

@router.post("/verifica-id")
def verify_id(payload: IDRequest):
    if id_exists(payload.id):
        return {"message": "ID Encontrado."}
    raise HTTPException(status_code=404, detail="ID  Nao Encontrado.")
