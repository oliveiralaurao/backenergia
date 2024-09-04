from fastapi import APIRouter, Query

from models.residencia import Residencia
from models.comodo import Comodo
from models.dispositivo import DispositivoDB
from schemas.consumo import ConsumoRead
from services.consumo import calcular_consumo
from utils.enuns import EnumOrigemDoConsumo
from utils.erros import (
    comodo_not_found_error,
    eletrodomestico_not_found_error,
    residencia_not_found_error,
)

router = APIRouter(prefix="/consumos", tags=["Consumos"])


@router.get("/", response_model=ConsumoRead)
def calcular_consumo_endpoint(
        origem_do_consumo: EnumOrigemDoConsumo = Query(...),
            item_id: int = Query(...),
):
    dispositivos_eletricos = []

    if origem_do_consumo == EnumOrigemDoConsumo.dispositivo_eletrico:
        dispositivos_eletricos = DispositivoDB.get_or_none(
            DispositivoDB.id == item_id
        )

        if not dispositivos_eletricos:
            raise eletrodomestico_not_found_error()

        dispositivos_eletricos = [dispositivos_eletricos]

    elif origem_do_consumo == EnumOrigemDoConsumo.comodo:
        comodo = Comodo.get_or_none(Comodo.id == item_id)
        if not comodo:
            raise comodo_not_found_error()

        dispositivos_eletricos = list(
            DispositivoDB.select().where(
                DispositivoDB.unidade_consumidora == comodo
            )
        )

    elif origem_do_consumo == EnumOrigemDoConsumo.residencia:
        residencia = Residencia.get_or_none(Residencia.id == item_id)
        if not residencia:
            raise residencia_not_found_error()

        dispositivos_eletricos = list(
            DispositivoDB.select().where(
                DispositivoDB.unidade_consumidora == residencia
            )
        )

    consumo_diario, consumo_mensal, consumo_anual = calcular_consumo(
        dispositivos_eletricos
    )

    return ConsumoRead(
        consumo_diario=consumo_diario,
        consumo_mensal=consumo_mensal,
        consumo_anual=consumo_anual,
    )