from Sistema import System

lista_funcionarios = []




print("\nBem-vindo a lista de funcionários!\n")
print("****************************************************")

print("O que você deseja fazer?")
print("1. Criar Funcionário")
print("2. Listar Funcionários")
print("3. Atualizar Funcionário")
print("4. Deletar Funcionário")
print("5. Sair")
print("")

opcao_inicial = int(input("Digite o número correspondente ao que deseja fazer: "))
while (opcao_inicial !=5 ):
    match opcao_inicial:
        case 1:
            System.criarFuncionario(lista_funcionarios)
        
        case 2:
            System.listarFuncionarios(lista_funcionarios)
            
        case 3:
            System.atualizarFuncionario(lista_funcionarios)

        case 4:
            System.deletarFuncionario(lista_funcionarios)

        case 5:
            break
        
        case _:
            print("Você digitou o número errado")

    print("O que você deseja fazer?")
    print("1. Criar Funcionário")
    print("2. Listar Funcionários")
    print("3. Atualizar Funcionário")
    print("4. Deletar Funcionário")
    print("5. Sair")


    opcao_inicial = int(input("Digite o número correspondente ao que deseja fazer: "))
    



