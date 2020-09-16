from Agencia import Agencia
from Banco import Banco
from ContaBanco import ContaBanco
from Pessoa import Pessoa

def main():
    banco_brasil = Banco("Banco do Brasil", 1808)
    ag1 = Agencia("1212-1")
    ag2 = Agencia("3434-3")
    banco_brasil.adicionar_agencia(ag1)
    banco_brasil.adicionar_agencia(ag2)
    pessoa1 = Pessoa("Seu Madruga", "111.222.333-44", "02/09/1923")
    cb1 = ContaBanco(pessoa1, 'X')
    ag1.criar_conta(cb1)
    cb1.depositar(580.00)
    cb1.sacar(430)

    pessoa2 = Pessoa("Chaves", "555.666.777-88", "21/02/1929")
    cb2 = ContaBanco(pessoa2, 'P')
    ag1.criar_conta(cb2)
    cb2.depositar(250.00)

    pessoa3 = Pessoa("Florinda", "000.999.999-00", "08/02/1949")
    cb3 = ContaBanco(pessoa3, 'C')
    ag2.criar_conta(cb3)
    cb3.depositar(500.00)

    pessoa4 = Pessoa("Clotilde", "717.171.717-71", "09/07/1922")
    cb4 = ContaBanco(pessoa4, 'C')
    ag2.criar_conta(cb4)
    cb4.depositar(1800)

    banco_brasil.listar_agencias()

main()