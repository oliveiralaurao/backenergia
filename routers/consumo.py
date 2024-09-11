from fastapi import APIRouter, Query, HTTPException

from models.dependencia import DependenciaDB
from models.dispositivo import DispositivoDB
from models.bandeira import BandeiraDB
from models.unidade_consumidora import UnidadeConsumidoraDB
from schemas.consumo import ConsumoRead
from schemas.bandeira import BandeiraRead
from services.consumo import calcular_consumo
from utils.enuns import EnumOrigemDoConsumo
from utils.erros import (
    comodo_not_found_error,
    eletrodomestico_not_found_error,
    unidade_consumidora_not_found_error  # Agora corretamente importado
)

router = APIRouter(prefix='/consumos', tags=['Consumos'])


@router.get('/', response_model=ConsumoRead)
def calcular_consumo_endpoint(
    origem_do_consumo: EnumOrigemDoConsumo = Query(...),
    item_id: int = Query(...),
    bandeira_id: int = Query(...)  # Novo campo para receber a bandeira
):
    dispositivos_eletricos = []

    if origem_do_consumo == EnumOrigemDoConsumo.dispositivo_eletrico:
        dispositivo_eletrico = DispositivoDB.get_or_none(
            DispositivoDB.id == item_id
        )

        if not dispositivo_eletrico:
            raise eletrodomestico_not_found_error()

        dispositivos_eletricos = [dispositivo_eletrico]

    elif origem_do_consumo == EnumOrigemDoConsumo.comodo:  # Atualizado para dependencia
        dependencia = DependenciaDB.get_or_none(DependenciaDB.id == item_id)
        if not dependencia:
            raise comodo_not_found_error()  # Mantido, mas agora refere-se a dependencia

        dispositivos_eletricos = list(
            DispositivoDB.select().where(
                DispositivoDB.dependencia == dependencia
            )
        )

    elif origem_do_consumo == EnumOrigemDoConsumo.residencia:  # Atualizado para unidade_consumidora
        unidade_consumidora = UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == item_id)
        if not unidade_consumidora:
            raise unidade_consumidora_not_found_error()

        dispositivos_eletricos = list(
            DispositivoDB.select().where(
                DispositivoDB.unidade_consumidora == unidade_consumidora
            )
        )

    # Obtendo a bandeira tarifária
    bandeira = BandeiraDB.get_or_none(BandeiraDB.id == bandeira_id)
    if not bandeira:
        raise HTTPException(status_code=404, detail="Bandeira não encontrada")

    # Calculando o consumo com a bandeira
    consumo_diario, consumo_mensal, consumo_anual, custo_diario, custo_mensal, custo_anual = calcular_consumo(
        dispositivos_eletricos, bandeira
    )

    return ConsumoRead(
        consumo_diario=consumo_diario,
        consumo_mensal=consumo_mensal,
        consumo_anual=consumo_anual,
        custo_diario=custo_diario,
        custo_mensal=custo_mensal,
        custo_anual=custo_anual
    )
