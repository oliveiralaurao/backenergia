from fastapi import APIRouter
from models.tipo_dispositivo import TipoDispositivoDB
from schemas.tipo_dispositivo import TipoDispositivoCreate, TipoDispositivoRead, TipoDispositivoReadList, TipoDispositivoUpdate

router = APIRouter(prefix='/tipos-dispositivos', tags=['TIPOS DE DISPOSITIVOS'])

@router.post(path='', response_model=TipoDispositivoRead)
def criar_tipo_dispositivo(novo_tipo_dispositivo: TipoDispositivoCreate):
    tipo_dispositivo = TipoDispositivoDB.create(**novo_tipo_dispositivo.model_dump())
    return tipo_dispositivo

@router.get(path='', response_model=TipoDispositivoReadList)
def listar_tipos_dispositivos():
    tipos_dispositivos = TipoDispositivoDB.select()
    return {'tipos_dispositivos': tipos_dispositivos}

@router.get(path='/{tipo_dispositivo_id}', response_model=TipoDispositivoRead)
def listar_tipo_dispositivo(tipo_dispositivo_id: int):
    tipo_dispositivo = TipoDispositivoDB.get_or_none(TipoDispositivoDB.id == tipo_dispositivo_id)
    return tipo_dispositivo

@router.patch(path='/{tipo_dispositivo_id}', response_model=TipoDispositivoRead)
def atualizar_tipo_dispositivo(tipo_dispositivo_id: int, tipo_dispositivo_atualizado: TipoDispositivoUpdate):
    tipo_dispositivo = TipoDispositivoDB.get_or_none(TipoDispositivoDB.id == tipo_dispositivo_id)
    tipo_dispositivo.nome = tipo_dispositivo_atualizado.nome
    tipo_dispositivo.save()
    return tipo_dispositivo

@router.delete(path='/{tipo_dispositivo_id}', response_model=TipoDispositivoRead)
def excluir_tipo_dispositivo(tipo_dispositivo_id: int):
    tipo_dispositivo = TipoDispositivoDB.get_or_none(TipoDispositivoDB.id == tipo_dispositivo_id)
    tipo_dispositivo.delete_instance()
    return tipo_dispositivo
