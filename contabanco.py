class ContaBanco():
    def __init__(self, nome_banco, agencia, conta, nome_titular, tipo, saldo, limite_saque):
        self.nome_banco = nome_banco
        self.agencia = agencia
        self.conta = conta
        self.nome_titular = nome_titular
        self.tipo = tipo
        self.saldo = saldo
        self.limite_saque = limite_saque
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo and valor <= self.limite_saque:
            self.saldo -= valor
        else:
            print("Não foi possível sacar o valor")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Não foi possível depositar o valor")

    def imprimir_dados(self):
        return ('''
            Informações sobre a conta:
            Nome do banco: {}
            Número da agência: {}
            Número da conta: {}
            Nome do titular: {}
            Tipo: {}
            Saldo: R${}
            Limite de saque: R${}
        '''.format(
            self.nome_banco,
            self.agencia,
            self.conta,
            self.nome_titular,
            self.tipo,
            self.saldo,
            self.limite_saque
        ))

def main():
    conta1 = ContaBanco("Nubank", 0000, 1111, "Godofredo", "P", 2000, 1000)

    print("Saldo inicial da conta: R${}".format(conta1.saldo))
    conta1.sacar(1000)
    print("Após o saque de R$1000, Saldo na conta: R${}".format(conta1.saldo))

    conta1.depositar(10)
    print("Saldo da conta após o deposito de R$10: R${}".format(conta1.saldo))

    infos_conta = conta1.imprimir_dados()
    print(infos_conta)
main()