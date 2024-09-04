from fastapi import status
from fastapi.responses import JSONResponse

def eletrodomestico_delete_message():
    return JSONResponse(
        content={'message': 'Eletrodoméstico deletado com sucesso!'},
        status_code=status.HTTP_202_ACCEPTED,
    )

def comodo_deleted_message():
    return JSONResponse(
        content={'message': 'Cômodo deletado com sucesso!'},
        status_code=status.HTTP_202_ACCEPTED,
    )

def residencia_deleted_message():
    return JSONResponse(
        content={'message': 'Residência deletada com sucesso!'},
        status_code=status.HTTP_202_ACCEPTED,
    )
