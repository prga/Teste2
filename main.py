from Conta import Conta
from Banco import Banco

def main():
    c1 = Conta(1)
    c2 = Conta(2)
    c3 = Conta(3)
    banco = Banco("Banco")
    banco.insere_conta(c1)
    banco.insere_conta(c2)
    banco.insere_conta(c3)
    banco.insere_conta(c3)
    banco.deposito(1, 100.00)
    banco.saque(2, 150.00)
    banco.saque(1, 50.00)
    banco.remove_conta(1)
    banco.remove_conta(5)


main()