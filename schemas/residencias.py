from pydantic import BaseModel
from schemas.comodos import ComodoRead

class ResidenciaCreate(BaseModel):
    proprietario: str

class ResidenciaUpdate(BaseModel):
    proprietario: str | None

class ResidenciaRead(BaseModel):
    id: int
    proprietario: str
    comodos: list[ComodoRead] = []

    class Config:
        from_attributes = True
