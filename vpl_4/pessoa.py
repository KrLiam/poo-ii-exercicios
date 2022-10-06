from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa


class Pessoa(AbstractPessoa, ABC):
    def __init__(self, nome: str, codigo: int):
        self.__codigo = codigo
        self.__nome = nome

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome
