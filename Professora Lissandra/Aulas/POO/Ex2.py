class Pessoa:
    

    def __init__(self, nome, idade, endereco, cpf, sexo):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.sexo = sexo
        
    def resumo(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Endereço: ", self.endereco)
        print("CPF: ", self.cpf)
        print("Sexo: ", self.sexo)
    


class Pai(Pessoa):
    filhos = ""
    esposa = ""
    def __init__(self, nome, idade, endereco, cpf, sexo ):
        super().__init__(nome, idade, endereco, cpf, sexo)
        

    def resumo(self):
        super().resumo(self)
        print("Filhos: ", self.filhos)
        print("Esposa: ", self.esposa)

    def adicionarFilho(self, filhos):
        self.filhos = filhos
    def adicionarEsposa(self, Esposa):
        self.esposa = Esposa

class Mae(Pessoa):

    def __init__(self, nome, idade, endereco, cpf, sexo):
        super().__init__(nome, idade, endereco, cpf, sexo)

    def resumo(self):
        super().resumo(self)
        print("Filhos: ", self.filhos)
        print("Marido: ", self.marido)

    def adicionarFilho(self, filhos):
        self.filhos = filhos

    def adicionarMarido(self, Marido):
        self.marido = Marido


class Filho(Mae, Pai):
    
   



    def resumo(self):
        super().resumo(self)
        print("Pai: ", self.pai)
        print("Mãe: ", self.mae)

    def adicionarMaePai(self, Mae, Pai):
        self.mae = Mae
        self.pai = Pai
    



Katiane =  Mae("Katiane", 41, "Rua Brasil", 111111111, "feminino")
Rafael = Pai("Rafael", 40, "Rua Brasil", 0000000000, "Masculino")
Luiz = Filho("Luiz", 21, "Rua Brasil", 222222222, "Masculino")

Katiane.adicionarFilho(Luiz)
Katiane.adicionarMarido(Rafael)

Rafael.adicionarFilho(Luiz)
Rafael.adicionarEsposa(Katiane)

Luiz.adicionarMaePai(Katiane, Rafael)

