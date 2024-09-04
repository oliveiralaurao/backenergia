from fastapi import APIRouter, Query
from models.residencia import Residencia
from schemas.residencias import (
    ResidenciaCreate,
    ResidenciaRead,
    ResidenciaUpdate,
)
from utils.erros import residencia_not_found_error
from utils.messages import residencia_deleted_message

router = APIRouter(prefix='/residencias', tags=['Residências'])


@router.post('/', response_model=ResidenciaRead)
def create_residencia(residencia: ResidenciaCreate):
    new_residencia = Residencia.create(**residencia.model_dump())
    return new_residencia
@router.get("/list", response_model=list[ ResidenciaRead])
def listar_residencias():
    residencias = ResidenciaRead.select()
    return residencias
@router.get('/', response_model=ResidenciaRead | list[ResidenciaRead])
def get_residencia(
    residencia_id: int | None = Query(None),
):
    if residencia_id:
        residencia = Residencia.get_or_none(Residencia.id == residencia_id)
        if not residencia:
            return residencia_not_found_error()
        return residencia

    residencias = Residencia.select()
    return residencias

@router.put('/{residencia_id}', response_model=ResidenciaRead)
def update_residencia(residencia_id: int, residencia_data: ResidenciaUpdate):
    residencia = Residencia.get_or_none(Residencia.id == residencia_id)

    if not residencia:
        return residencia_not_found_error()

    residencia.proprietario = (
        residencia_data.proprietario or residencia.proprietario
    )
    residencia.save()
    return residencia

@router.delete('/{residencia_id}')
def delete_residencia(residencia_id: int):
    residencia = Residencia.get_or_none(Residencia.id == residencia_id)

    if not residencia:
        return residencia_not_found_error()

    residencia.delete_instance()
    return residencia_deleted_message()
