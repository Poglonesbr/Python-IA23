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
    


class System ():
       

    # Criar funcionario e adicionar informações
    def criarFuncionario(lista_funcionarios):
        print("Digite as informações necessárias:")
        _nome = input("Nome: ")
        _cargo = input("Cargo: ")
        _salario = float(input("Salario: "))
        _cpf = input("CPF: ")
        
        ano_contratacao = int(input("Digite o ano de contratação: ")) 
        mes_contratacao = int(input("Digite o mês de contratação: "))
        dia_contratacao = int(input("Digite o dia de contratação: "))
        _data_contratacao = datetime.datetime(ano_contratacao, mes_contratacao, dia_contratacao)

        
        lista_funcionarios.append(Funcionario(_nome, _cargo, _salario, _cpf, _data_contratacao) )
        

    # Não sei como fazer
    def listarFuncionarios(lista_funcionarios):
        print("\nLista de FUNCIONÁRIOS: \n")
        for i in range (0, len(lista_funcionarios)):
            print(lista_funcionarios[i].nome)
            print("   Cargo:", lista_funcionarios[i].cargo)
            print("   Salário:", lista_funcionarios[i].salario)
            print("   CPF:", lista_funcionarios[i].cpf)
            print("   Data da Contratação:", lista_funcionarios[i].data_contratacao)

    def atualizarFuncionario(lista_funcionarios):
        System.listarFuncionarios(lista_funcionarios)
        escolherNome = input("Digite o nome do funcionário que deseja atualizar: ")
        for i in range (0, len(lista_funcionarios)):
            if(escolherNome == lista_funcionarios[i].nome):
                print("Qual informação você deseja atualizar?")
                print("1. Nome")
                print("2. Cargo")
                print("3. Salário")
                print("4. CPF")
                print("5. Data de Contratação")
                print("6. Cancelar Atualização")
                print("----------------------------------------------------")
                _opcao = int(input("Digite o numero correspondente à ação que deseja fazer: "))

                match _opcao:
                        case 1:
                            _nome = input("Digite o nome atualizado do funcionario: ")
                            lista_funcionarios[i].setNomeFunc(_nome)
                        case 2:
                            _cargo = input("Digite o cargo atualizado do funcionario: ")
                            lista_funcionarios[i].setCargoFunc(_cargo)
                        case 3:
                            _salario = int(input("Digite o salario atualizado do funcionario: "))
                            lista_funcionarios[i].setSalarioFunc(_salario)
                        case 4:
                            _cpf = input("Digite o CPF atualizado do funcionario:")
                            lista_funcionarios[i].setCPF(_cpf)
                        case 5:
                            ano_contratacao = int(input("Digite o ano de contratação: "))
                            mes_contratacao = int(input("Digite o mes de contratação: "))
                            dia_contratacao = int(input("Digite o dia de contratação: "))
                            _data_contratacao = datetime.datetime(ano_contratacao, mes_contratacao, dia_contratacao)
                            lista_funcionarios[i].setDataContratacao(_data_contratacao)
                        case 6:
                            print("Saindo")
                        case _:
                            print("O numero digitado não corresponde as opções acima, digite novamente")
                            System.atualizarFuncionario(lista_funcionarios)
        print("O nome digitado não existe.")
                
    
    def deletarFuncionario(lista_funcionarios):
        nomeRemover = input("Digite o nome do funcionário que deseja deletar: ")
        for i in range (0, len(lista_funcionarios)):
            if(nomeRemover == lista_funcionarios[i].nome):
                del lista_funcionarios[i]
                


    
    