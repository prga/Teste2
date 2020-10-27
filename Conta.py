class Conta:

    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0

    def mostraSaldo(self):
        print('O seu saldo é de R${:.2f}'.format(self.saldo))

    def saque(self, valor):
        if(valor <= self.saldo):
            self.saldo -= valor
            print('Saque realizado com sucesso.')
        else:
            print('Você não possui saldo para realizar o saque nesse valor.')
        self.mostraSaldo()

    def deposito(self, valor):
        if(valor > 0):
            self.saldo += valor
            print('Depósito realizado com sucesso.')
        else:
            print('Valor inválido para depósito')
        self.mostraSaldo()



