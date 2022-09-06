
class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

class Aluno(Pessoa):
    def __init__(self, nome: str, email: str):
        super().__init__(nome)
        self.__email = email
        self.__iaa = 0
    
    @property
    def iaa(self):
        return self.__iaa
    
    @property
    def email(self):
        return self.__email


class Professor(Pessoa):
    def __init__(self):
        ...


class Turma:
    def __init__(self, disciplina: str):
        self.disciplina = disciplina
    
    def matricular_aluno(self, aluno: Aluno):
        self.__alunos


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
        aluno = Aluno(nome, email)
        matricula = self.gerar_id()

        self.__alunos[matricula] = aluno

        return aluno

    def cadastrar_professor(self, nome: str):
        professor = Professor(nome)
        matricula = self.gerar_id()

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
