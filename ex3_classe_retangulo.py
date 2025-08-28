class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        print (f"A área é de {self.altura * self.largura:.2f}")

    def perimetro(self):
        print(f"O perímetro é de {2*(self.altura + self.largura):.2f}")

retangulo = Retangulo(5, 3)

retangulo.area()
retangulo.perimetro()