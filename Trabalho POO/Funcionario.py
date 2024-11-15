import datetime

class Funcionario:
    # Construtor
    def __init__(self, _nome, _cargo, _salario, _cpf, _data_contratacao): 
        self.nome = _nome
        self.cargo = _cargo
        self.salario = _salario
        self.cpf = _cpf
        self.data_contratacao = _data_contratacao

    #Gets e Sets
    def setNomeFunc(self, _nome): 
        self.nome = _nome
    
    def getNomeFunc(self):
        return self.nome
    
    def setCargoFunc(self, _cargo):
        self.cargo = _cargo

    def getCargoFunc(self):
        return self.cargo

    def setSalarioFunc(self, _salario):
        self.salario = _salario

    def getSalarioFunc(self):
        return self.salario

    def setCPF(self, _cpf):
        self.cpf = _cpf

    def getCPF(self):
        return self.cpf
    
    def setDataContratacao(self, _data_contratacao): # Talvez tenha editar 
        self.data_contratacao = _data_contratacao
    
    def getDataContratacao(self):
        return self.data_contratacao
    
# Lista de Funcionarios, não lembro qual é o correto a utilizar     
Funcionarios = []

# Criar funcionario e adicionar informações
def criarFuncionario(Funcionarios):
    print("Digite as informções necessárias:")
    _nome = input("Nome: ")
    _cargo = input("Cargo: ")
    _salario = float(input("Salario: "))
    _cpf = input("CPF: ")
    
    ano_contratacao = int(input("Digite o ano de contratação: "))
    mes_contratacao = int(input("Digite o mes de contratação: "))
    dia_contratacao = int(input("Digite o dia de contratação: "))
    _data_contratacao = datetime(ano_contratacao, mes_contratacao, dia_contratacao)

    funcionario = Funcionario(_nome, _cargo, _salario, _cpf, _data_contratacao) 
    Funcionarios = Funcionarios.append

# Não sesi como fazer
def listarFuncionarios(Funcionarios):
    print(Funcionarios)

def atualizarFuncionario(funcionario):
    print("Qual informação você deseja atualizar?")
    print("1. Nome")
    print("2. Cargo")
    print("3. Salario")
    print("4. CPF")
    print("5. Data de Contratação")
    print("6. Cancelar Atualização")
    print("----------------------------------------------------")
    _opcao = int(input("Digite o numero correspondente à ação que deseja fazer: "))

    match _opcao:
        case 1:
            _nome = input("Digite o nome atualizado do funcionario: ")
            funcionario.setNome(_nome)
        case 2:
            _cargo = input("Digite o cargo atualizado do funcionario: ")
            funcionario.setCargo(_cargo)
        case 3:
            _salario = int(input("Digite o salario atualizado do funcionario: "))
            funcionario.setSalario(_salario)
        case 4:
            _cpf = input("Digite o CPF atualizado do funcionario:")
            funcionario.setCPF(_cpf)
        case 5:
            ano_contratacao = int(input("Digite o ano de contratação: "))
            mes_contratacao = int(input("Digite o mes de contratação: "))
            dia_contratacao = int(input("Digite o dia de contratação: "))
            _data_contratacao = datetime(ano_contratacao, mes_contratacao, dia_contratacao)
            funcionario.setDataContrataca(_data_contratacao)
        case 6:
            menu()
        case _:
            print("O numero digitado não corresponde as opções acima, digite novamente")
            menu()
        
# Mensagem Inicial
def mensagemInicio():
    print("Bem vindo a lista de funcionarios\n")
    print("****************************************************")

# Menu principal para as ações
def menu(funcionario, Fucionarios):     
    print("O que você deseja fazer?")
    print("1. Criar Funcionario")
    print("2. Listar Funcionarios")
    print("3. Atualizar Funcionario")
    print("4. Deletar Funcionario")
    print("5. Sair")

    opcao_inicial = int(input("Digite o numero correspondente ao que deseja fazer: "))

    match opcao_inicial:
        case 1:
            criarFuncionario(Funcionarios)
        
        case 2:
            listarFuncionarios(Funcionarios)
            
        case 3:
            atualizarFuncionario(funcionario)

