class ContaBanco():
    _id_conta = 0

    def __init__(self, titular, tipo_conta):
        self.titular = titular
        self.tipo_conta = tipo_conta
        self._saldo = 0.0
        self._limite_saque = 1000.0
        #Incremento do inicializador
        ContaBanco._id_conta += 1
        self._num_conta = ContaBanco._id_conta

    @property
    def tipo_conta(self):
        return self._tipo_conta
    @tipo_conta.setter 
    def tipo_conta(self, tipo):
        tipo_convert = str(tipo).upper()
        if tipo_convert == "C" or tipo_convert == "P":
            self._tipo_conta = tipo_convert
        else:
            self._tipo_conta = "P"
    
    @property
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo and valor <= self._limite_saque:
            self._saldo -= valor
        else:
            print("Não foi possível sacar o valor")

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("Não foi possível depositar o valor")

    def exibir_info(self):
        return ('''
            Informações sobre a conta:
            Titular: {}
            Numero da conta: {}
            Tipo da conta: {}
            Saldo: R${}
            Limite de saque R$: {}
        '''.format(
            self.titular.nome_completo,
            self._num_conta,
            self._tipo_conta,
            self.saldo,
            self._limite_saque
        ))
