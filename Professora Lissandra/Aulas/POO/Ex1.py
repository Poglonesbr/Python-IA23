# Implementar os métodos abaixo para a classe Carro: #a.ligarMotor# b.desligarMotor# c.andar# d.parar


class Carro:
    def __init__(self, marca, modelo, ano, cor, km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.kmRodados = km


    gasolina = 20
    acelerar = False

# Criar atributos para Status do motor(ligado / desligado)
    def ligarMotor(self, ligado):
        self.ligado = True
        return

    def desligarMotor(self, ligado):
        self.ligado = False
        return
# b.Status do movimento do carro(andando / parado)
    def andar(self, ligado, gasolina, acelerar):
        if ligado and gasolina > 0 and acelerar:
            self.andando = True

    def parar(self, ligado, gasolina, acelerar):
        if ligado == False or gasolina == 0 or acelerar == False:
            self.andando = self.FALSE

#Criar métodos para informar (exibir na tela) o status acima.
    def exibirDetalhes(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Ano: ", self.ano)
        print("Cor: ", self.cor)

    def adicionarKmRodados(self, km):
        self.kmRodados += km

meu_carro = Carro("Toyota", "Corolla", 2020, "azul", 0)



meu_carro.ligarMotor(True)
meu_carro.desligarMotor(True)
meu_carro.andar(True, 20, True)
meu_carro.parar(True, 20, False)