
from typing import Iterable


class Pessoa:
    def __init__(self, id: int, nome: str):
        self.__id = id
        self.__nome = nome

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome


class Aluno(Pessoa):
    def __init__(self, id: int, nome: str, email: str):
        super().__init__(id, nome)
        self.__email = email
        self.__iaa = 0
    
    @property
    def iaa(self):
        return self.__iaa
    
    @property
    def email(self):
        return self.__email


class Professor(Pessoa):
    def __init__(self, id: int, nome: str):
        super().__init__(id, nome)


class Turma:
    def __init__(self, disciplina: str):
        self.__disciplina = disciplina
        self.__profs = set()
        self.__alunos = set()
    
    @property
    def disciplina(self): return self.__disciplina

    @property
    def professores(self): return self.__profs

    @property
    def alunos(self): return self.__alunos
    
    def matricular_aluno(self, aluno: Aluno):
        self.__alunos.add(aluno)

    def matricular_professor(self, professor: Professor):
        self.__profs.add(professor)


class Gerenciador:
    def __init__(self):
        self.__alunos = {}
        self.__professores = {}
        self.__turmas = {}

        self.__id = 0
    
    def gerar_id(self):
        self.__id += 1
        return self.__id        
    
    def cadastrar_aluno(self, nome: str, email: str):
        matricula = self.gerar_id()
        aluno = Aluno(matricula, nome, email)

        self.__alunos[matricula] = aluno

        return aluno

    def cadastrar_professor(self, nome: str):
        matricula = self.gerar_id()
        professor = Professor(matricula, nome)

        self.__professores[matricula] = professor

        return professor
    
    def cadastrar_turma(self, disciplina: str):
        turma = Turma(disciplina)
        self.__turmas[disciplina] = turma
        return turma


if __name__ == "__main__":

    gerenciador = Gerenciador()

    turma_calculo = gerenciador.cadastrar_turma("mtm3120")
    print(turma_calculo)

    fulano = gerenciador.cadastrar_aluno("Fulano", "fulano123@gmail.com")
    print(fulano)
