#Definindo a classe
class Pessoa:
    def __init__(self, nome, idade):
        self.none = NotImplemented
        self.idade = idade
    
def apresentar (self):
    self.idade += 1
    print(f"Parabéns {self.nome}! Agora você tem {self.idade} anos.")

#Criando objetos

p1 = Pessoa ("Ana", 25)
p2 = Pessoa ("Carlos", 30)

#Chamando os métodos
p1.apresentar()
p1.fazer_aniversario()
p1.apresentar()

print("---")

p2.apresentar()
p2.fazer_aniversario()
p2.apresentar()
