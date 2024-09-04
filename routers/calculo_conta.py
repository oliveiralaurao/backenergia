from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/calcular-conta")
async def calcular_conta(consumo: float, tarifa_basica: float, percentual_bandeira: float):
    if consumo < 0 or tarifa_basica < 0 or percentual_bandeira < 0:
        raise HTTPException(status_code=400, detail="Valores de entrada devem ser positivos")

    valor_conta = (consumo * tarifa_basica) + (consumo * tarifa_basica * percentual_bandeira)
    return {"valor_conta": valor_conta}
