from abstractChamado import AbstractChamado
from tipoChamado import TipoChamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class Chamado(AbstractChamado):
    def __init__(
        self,
        data: Date,
        cliente: Cliente,
        tecnico: Tecnico,
        titulo: str,
        descricao: str,
        prioridade: int,
        tipo: TipoChamado
    ):
        self.data = data
        self.cliente = cliente
        self.tecnico = tecnico
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.tipo = tipo