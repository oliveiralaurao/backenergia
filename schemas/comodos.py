from pydantic import BaseModel
from schemas.dispositivos import EletrodomesticoRead

class ComodoCreate(BaseModel):
    nome: str
    residencia_id: int

class ComodoUpdate(BaseModel):
    nome: str | None

class ComodoRead(BaseModel):
    id: int
    nome: str
    residencia_id: int
    eletrodomesticos: list[EletrodomesticoRead] = []

    class Config:
        from_attributes = True
