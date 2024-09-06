from fastapi import HTTPException

def comodo_not_found_error():
    return HTTPException(status_code=404, detail="Dependência não encontrada")

def eletrodomestico_not_found_error():
    return HTTPException(status_code=404, detail="Dispositivo elétrico não encontrado")

def unidade_consumidora_not_found_error():  # Novo erro
    return HTTPException(status_code=404, detail="Unidade consumidora não encontrada")
