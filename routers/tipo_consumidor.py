from fastapi import APIRouter
from models.tipo_consumidor import TipoConsumidorDB
from schemas.tipo_consumidor import TipoConsumidorCreate, TipoConsumidorRead, TipoConsumidorReadList, TipoConsumidorUpdate

router = APIRouter(prefix='/tipos-consumidores', tags=['TIPOS DE CONSUMIDORES'])

@router.post(path='', response_model=TipoConsumidorRead)
def criar_tipo_consumidor(novo_tipo_consumidor: TipoConsumidorCreate):
    tipo_consumidor = TipoConsumidorDB.create(**novo_tipo_consumidor.model_dump())
    return tipo_consumidor

@router.get(path='', response_model=TipoConsumidorReadList)
def listar_tipos_consumidores():
    tipos_consumidores = TipoConsumidorDB.select()
    return {'tipos_consumidores': tipos_consumidores}

@router.get(path='/{tipo_consumidor_id}', response_model=TipoConsumidorRead)
def listar_tipo_consumidor(tipo_consumidor_id: int):
    tipo_consumidor = TipoConsumidorDB.get_or_none(TipoConsumidorDB.id == tipo_consumidor_id)
    return tipo_consumidor

@router.patch(path='/{tipo_consumidor_id}', response_model=TipoConsumidorRead)
def atualizar_tipo_consumidor(tipo_consumidor_id: int, tipo_consumidor_atualizado: TipoConsumidorUpdate):
    tipo_consumidor = TipoConsumidorDB.get_or_none(TipoConsumidorDB.id == tipo_consumidor_id)
    tipo_consumidor.nome = tipo_consumidor_atualizado.nome
    tipo_consumidor.valor_kwh = tipo_consumidor_atualizado.valor_kwh
    tipo_consumidor.save()
    return tipo_consumidor

@router.delete(path='/{tipo_consumidor_id}', response_model=TipoConsumidorRead)
def excluir_tipo_consumidor(tipo_consumidor_id: int):
    tipo_consumidor = TipoConsumidorDB.get_or_none(TipoConsumidorDB.id == tipo_consumidor_id)
    tipo_consumidor.delete_instance()
    return tipo_consumidor
