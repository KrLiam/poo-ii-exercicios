from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = {}
        self.__tecnicos = {}

    # @return retorna a lista de clientes
    @property
    def clientes(self) -> list:
        return list(self.__clientes.values())

    # @return retorna a lista de tecnicos
    @property
    def tecnicos(self) -> list:
        return list(self.__tecnicos.values())

    # Permite a inclusao de um novo cliente na lista de clientes
    # @param codigo codigo do Cliente
    # @param nome nome do Cliente
    # @return retorna o cliente inserido como um IPessoa
    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        if codigo in self.__clientes:
            return

        cliente = Cliente(nome, codigo)
        self.__clientes[codigo] = cliente

        return cliente

    # Permite a inclusao de um novo tecnico na lista de tecnicos
    # @param codigo codigo do tecnico
    # @param nome nome do tecnico
    # @return retorna o tecnico inserido como um IPessoa
    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        if codigo in self.__tecnicos:
            return

        tecnico = Tecnico(nome, codigo)
        self.__tecnicos[codigo] = tecnico

        return tecnico
