from fastapi import APIRouter
from models.dependencia import DependenciaDB, UnidadeConsumidoraDB
from schemas.dependencia import DependenciaCreate, DependenciaReadList, DependenciaReadOne, DependenciaUpdate

router = APIRouter(prefix='/dependencias', tags=['DEPENDÊNCIAS'])

@router.post(path='', response_model=DependenciaReadOne)
def criar_dependencia(nova_dependencia: DependenciaCreate):
    dependencia = DependenciaDB.create(**nova_dependencia.model_dump())
    return dependencia

@router.get(path='/unidade-consumidora/{unidade_consumidora_id}', response_model=DependenciaReadList)
def listar_dependencia_da_unidade_de_consumo(unidade_consumidora_id: int):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == unidade_consumidora_id)
    dependencias = DependenciaDB.select().where(DependenciaDB.unidade_consumidora == unidade_consumidora)
    return {'dependencias': dependencias}

@router.get(path='/{dependencia_id}', response_model=DependenciaReadOne)
def listar_dependencia(dependencia_id: int):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    return dependencia

@router.patch(path='/{dependencia_id}', response_model=DependenciaReadOne)
def atualizar_dependencia(dependencia_id: int, dependencia_atualizada: DependenciaUpdate):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    dependencia.nome = dependencia_atualizada.nome
    dependencia.save()
    return dependencia

@router.delete(path='/{dependencia_id}', response_model=DependenciaReadOne)
def excluir_dependencia(dependencia_id: int):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    dependencia.delete_instance()
    return dependencia
