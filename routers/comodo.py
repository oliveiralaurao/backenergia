from fastapi import APIRouter, Query
from models.comodo import Comodo
from models.residencia import Residencia
from schemas.comodos import ComodoCreate, ComodoRead, ComodoUpdate
from utils.enuns import EnumGetComodos
from utils.erros import comodo_not_found_error, residencia_not_found_error
from utils.messages import comodo_deleted_message

router = APIRouter(prefix='/comodos', tags=['Cômodos'])

@router.post('/', response_model=ComodoRead)
def create_comodo(comodo: ComodoCreate):
    residencia = Residencia.get_or_none(Residencia.id == comodo.residencia_id)
    if not residencia:
        raise residencia_not_found_error()

    new_comodo = Comodo.create(nome=comodo.nome, residencia=residencia)
    return new_comodo

@router.put('/{comodo_id}', response_model=ComodoRead)
def update_comodo(comodo_id: int, comodo_data: ComodoUpdate):
    comodo = Comodo.get_or_none(Comodo.id == comodo_id)
    if not comodo:
        raise comodo_not_found_error()

    comodo.nome = comodo_data.nome or comodo.nome
    comodo.save()
    return comodo

@router.delete('/{comodo_id}')
def delete_comodo(comodo_id: int):
    comodo = Comodo.get_or_none(Comodo.id == comodo_id)
    if not comodo:
        raise comodo_not_found_error()

    comodo.delete_instance()
    return comodo_deleted_message()

@router.get('/', response_model=ComodoRead | list[ComodoRead])
def get_comodos_by_residencia(
        item_type: EnumGetComodos = Query(...),
        item_id: int = Query(...),
):
    if item_type == EnumGetComodos.residencia:
        residencia = Residencia.get_or_none(Residencia.id == item_id)
        if not residencia:
            raise residencia_not_found_error()
        comodos = Comodo.select().where(Comodo.residencia == residencia)
        return list(comodos)

    elif item_type == EnumGetComodos.comodo:
        comodo = Comodo.get_or_none(Comodo.id == item_id)
        if not comodo:
            raise comodo_not_found_error()
        return comodo

    else:
        # Opcional: Defina um comportamento padrão ou retorne um erro se o item_type for inválido
        raise ValueError("Invalid item_type provided")
