from peewee import AutoField, CharField, DoubleField, ForeignKeyField, Model
from config.database import database
from models.dependencia import DependenciaDB
from models.tipo_dispositivo import TipoDispositivoDB
from models.unidade_consumidora import UnidadeConsumidoraDB


class DispositivoDB(Model):
    id = AutoField(column_name='dispositivo_id')
    nome = CharField(column_name='dispositivo_nome')
    consumo = DoubleField(column_name='dispositivo_consumo')
    uso_diario = DoubleField(column_name='dispositivo_uso_diario')

    tipo = ForeignKeyField(
        TipoDispositivoDB,
        column_name='dispositivo_tipo_id',
        backref='dispositivos'
    )

    dependencia = ForeignKeyField(
        DependenciaDB,
        column_name='dispositivo_dependencia_id',
        backref='dispositivos'
    )

    unidade_consumidora = ForeignKeyField(
        UnidadeConsumidoraDB,
        column_name='dispositivo_unidade_consumidora_id',
        backref='dispositivos'
    )

    class Meta:
        database = database
        table_name = 'dispositivos'
