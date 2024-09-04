from models.dispositivo import DispositivoDB

def calcular_consumo(eletrodomesticos: list[DispositivoDB]):
    consumo_diario = sum(
        eletrodomestico.consumo * eletrodomestico.uso_diario
        for eletrodomestico in eletrodomesticos
    )
    consumo_mensal = consumo_diario * 30
    consumo_anual = consumo_diario * 365

    return consumo_diario, consumo_mensal, consumo_anual
