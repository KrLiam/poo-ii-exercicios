from abstractTipoChamado import AbstractTipoChamado


class TipoChamado(AbstractTipoChamado):
    def __init__(self, codigo: int, descricao: str, nome: str):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__nome = nome
    
    @property
    def codigo(self):
        return self.__codigo
        
    @property
    def descricao(self):
        return self.__descricao
        
    @property
    def nome(self):
        return self.__nome
    
    def __eq__(self, val):
        if isinstance(val, TipoChamado):
            return self.__codigo == val.codigo
        
        return False
    
    def __hash__(self):
        return hash(self.__codigo)
