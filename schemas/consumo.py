from pydantic import BaseModel


class ConsumoRead(BaseModel):
    consumo_diario: float
    consumo_mensal: float
    consumo_anual: float