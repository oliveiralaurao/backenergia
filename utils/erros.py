from fastapi import HTTPException, status

def eletrodomestico_not_found_error():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Eletrodoméstico não encontrado',
    )

def comodo_not_found_error():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Cômodo não encontrado',
    )

def residencia_not_found_error():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Residência não encontrada',
    )
