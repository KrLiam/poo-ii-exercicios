from datetime import date as Date
from abstractControladorChamados import AbstractControladorChamados
from cliente import Cliente
from tecnico import Tecnico
from tipoChamado import TipoChamado
from chamado import Chamado


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.chamados = {}
    
    # Retorna o total de chamados registrados para o TipoChamado recebido como parametro
    # @param tipo TipoChamado
    # @return int com a quantidade total dos chamados daquele tipo
    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        return len(self.chamados.get(tipo, ()))

    # Permite incluir um novo chamado na lista de Chamados. O chamado incluido eh retornado como um IChamado
    # @param data data do chamado em formato Date
    # @param cliente referencia para o Cliente do chamado
    # @param tecnico referencia para o Tecnico do chamado
    # @param titulo titulo do chamado
    # @param descricao descricao do chamado
    # @param prioridade prioridade do chamado
    # @param tipo tipo do chamado (TipoChamado)
    # @return retorna o chamato cadastrado
    def incluiChamado(
        self,
        data: Date,
        cliente: Cliente,
        tecnico: Tecnico,
        titulo: str,
        descricao: str,
        prioridade: int,
        tipo: TipoChamado,
    ) -> Chamado:
        if not (
            isinstance(data, Date)
            and isinstance(cliente, Cliente)
            and isinstance(tecnico, Tecnico)
            and isinstance(titulo, str)
            and isinstance(descricao, str)
            and isinstance(prioridade, int)
            and isinstance(tipo, TipoChamado)
        ):
            return
        
        chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)

        chamados = self.chamados.setdefault(tipo, [])
        chamados.append(chamado)

        return chamado

    # Permite incluir um novo TipoChamado na lista de TiposChamado. O TipoChamado incluido eh retornado como um ITipoChamado
    # @param codigo codigo do Tipo Chamado
    # @param nome nome do Tipo Chamado
    # @param descricao descricao do Tipo Chamado
    # @return retorna o Tipo Chamado cadastrado
    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        tipo = TipoChamado(codigo, descricao, nome)

        if tipo not in self.chamados:
            self.chamados[tipo] = []
        
        return tipo

    @property
    def tipoChamados(self):
        return tuple(self.chamados.keys())