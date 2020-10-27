from Conta import Conta

class Banco:

    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def busca_Conta (self, numero):
        index = -1
        for i in range(0, len(self.contas)):
            if self.contas[i].numero == numero:
                return i
        return index


    def insere_conta(self, conta):
        index = self.busca_Conta(conta.numero)
        if index == -1:
            self.contas.append(conta)
            print("Conta inserida com sucesso!")
        else:
            print("Conta não foi criada porque já existe!")

    def deposito(self, numero, valor):
        index = self.busca_Conta(numero)
        if index != -1:
            self.contas[index].deposito(valor)
        else:
            print("Número de conta inválida!")

    def saque(self, numero, valor):
        index = self.busca_Conta(numero)
        if index != -1:
            self.contas[index].saque(valor)
        else:
            print("Número de conta inválida!")

    def remove_conta(self, numero):
        index = self.busca_Conta(numero)
        if index != -1:
            conta = self.contas[index]
            self.contas.remove(conta)
            print("Conta removida com sucesso!")
        else:
            print("Conta não removida porque não existe!")
