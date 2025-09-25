class contabancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar (self, valor):
        self.saldo += valor

    def sacar (self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo Insuficiente!")

    def exibir_saldo(self):
        print(f"O saldo de {self.titular} é de R${self.saldo:.2f}")

cliente1 = contabancaria("João", 1000)

cliente1.depositar(500)
cliente1.sacar(300)
cliente1.exibir_saldo()
