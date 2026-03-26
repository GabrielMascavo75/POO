class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []  # lista vazia no início

    def adicionar_nota(self, valor):
        self.notas.append(valor)

    def media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        if self.media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


# Testando conforme o exercício
aluno = Aluno("Maria")
aluno.adicionar_nota(8.0)
aluno.adicionar_nota(6.5)
aluno.adicionar_nota(7.5)

print(f"Média: {aluno.media():.2f}")
print(f"Situação: {aluno.situacao()}")
