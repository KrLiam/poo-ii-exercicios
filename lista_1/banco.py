from typing import Dict, List, Tuple


class Cliente:
    def __init__(self, nome: str, telefone: int):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone


class Conta:
    def __init__(self, titulares: Tuple[Cliente]):
        self.__titulares = titulares
        self.__saldo = 0

    @property
    def titulares(self):
        return self.__titulares

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor: float):
        self.__saldo += valor

    def sacar(self, valor: float):
        if valor > self.__saldo:
            raise ValueError("saldo insuficiente")

        self.__saldo -= valor


class ContaPoupanca(Conta):
    def __init__(self, *args, taxa=0, **kwargs):
        super().__init__(*args, **kwargs)

        self.__taxa_rendimento = taxa

    @property
    def taxa_rendimento(self):
        return self.__taxa_rendimento

    def render(self):
        self.depositar(self.saldo * self.__taxa_rendimento)


class Banco:
    def __init__(self, nome: str):
        self.__nome = nome

        self.__contas: List[Conta] = []
        self.__clientes: Dict[int, Cliente] = {}
        self.__taxa_rendimento = 0.065

    @property
    def nome(self):
        return self.__nome

    def cadastrar_cliente(self, nome: str, telefone: int):
        if nome in self.__clientes:
            raise ValueError(f"cliente '{nome}' já está cadastrado")

        cliente = Cliente(nome, telefone)
        self.__clientes[nome] = cliente

        return cliente

    def get_cliente(self, nome: str):
        return self.__clientes[nome]

    def abrir_conta(self, titulares: Tuple[Cliente], poupanca=False):
        if poupanca:
            conta = ContaPoupanca(titulares, taxa=self.__taxa_rendimento)
        else:
            conta = Conta(titulares)

        self.__contas.append(conta)

        return conta

    def get_contas(self, titular: Cliente):
        return tuple(conta for conta in self.__contas if titular in conta.titulares)

    def rendimento_mensal(self):
        for conta in self.__contas:
            if isinstance(conta, ContaPoupanca):
                conta.render()


if __name__ == "__main__":
    banco = Banco("Tatu")

    fulano = banco.cadastrar_cliente("Fulano de Tal", 48999887766)
    flavinho = banco.cadastrar_cliente("Flavinho do Pneu", 31415926535)

    try:
        banco.cadastrar_cliente("Fulano de Tal", 12312442112)
    except ValueError as e:
        print(e)

    conta = banco.abrir_conta((fulano, flavinho))

    print(conta.titulares)
    print(conta.saldo)

    try:
        conta.saldo = 1_000_000
    except AttributeError as e:
        print(e)

    conta.depositar(500)
    print(conta.saldo)

    conta.sacar(119.99)
    print(conta.saldo)

    try:
        conta.sacar(400)
    except ValueError as e:
        print(e)

    joao = banco.cadastrar_cliente("João Silva", 13987374627)
    poupanca_joao = banco.abrir_conta((joao,), poupanca=True)

    poupanca_joao.depositar(100)

    print(poupanca_joao.saldo)

    banco.rendimento_mensal()

    print(poupanca_joao.saldo)


    banco.abrir_conta((joao,))

    for conta in banco.get_contas(joao):
        print(f"{joao.nome} tem R${conta.saldo}")
