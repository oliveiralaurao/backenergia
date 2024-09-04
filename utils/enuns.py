from enum import Enum

class EnumGetEletrodomesticos(Enum):
    comodo = 'comodo'
    eletrodomestico = 'dispositivo_eletrico'
    residencia = 'residencia'

class EnumGetComodos(Enum):
    comodo = 'comodo'
    residencia = 'residencia'

class EnumOrigemDoConsumo(Enum):
    dispositivo_eletrico = 'dispositivo_eletrico'
    comodo = 'comodo'
    residencia = 'residencia'
