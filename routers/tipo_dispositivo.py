from fastapi import APIRouter

from models.tipo_dispositivo import TipoDispositivoDB
from schemas.tipo_dispositivo import (
    TipoDispositivoCreate,
    TipoDispositivoRead,
    TipoDispositivoReadList,
    TipoDispositivoUpdate,
)

router = APIRouter(
    prefix='/tipos-dispositivos', tags=['TIPOS DE DISPOSITIVOS']
)


@router.post(path='', response_model=TipoDispositivoRead)
def criar_tipo_de_dispositivo(novo_tipo: TipoDispositivoCreate):
    tipo = TipoDispositivoDB.create(**novo_tipo.model_dump())
    return tipo


@router.get(path='', response_model=TipoDispositivoReadList)
def listar_tipos_de_dispositivo():
    tipos = TipoDispositivoDB.select()
    return {'tipos_dispositivos': tipos}


@router.get(path='/{tipo_consumidor_id}', response_model=TipoDispositivoRead)
def listar_tipo_de_dispositivo(tipo_consumidor_id: int):
    tipo = TipoDispositivoDB.get_or_none(
        TipoDispositivoDB.id == tipo_consumidor_id
    )
    return tipo


@router.patch(path='/{tipo_consumidor_id}', response_model=TipoDispositivoRead)
def atualizar_tipo_de_dispositivo(
    tipo_consumidor_id: int, tipo_atualizado: TipoDispositivoUpdate
):
    tipo = TipoDispositivoDB.get_or_none(
        TipoDispositivoDB.id == tipo_consumidor_id
    )
    tipo.nome = tipo_atualizado.nome
    tipo.save()
    return tipo


@router.delete(
    path='/{tipo_consumidor_id}', response_model=TipoDispositivoRead
)
def excluir_tipo_de_dispositivo(tipo_consumidor_id: int):
    tipo = TipoDispositivoDB.get_or_none(
        TipoDispositivoDB.id == tipo_consumidor_id
    )
    tipo.delete_instance()
    return tipo