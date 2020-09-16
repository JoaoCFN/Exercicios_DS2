class Agencia():
    def __init__(self, numero):
        self.numero = numero
        self._lista_conta = []

    def criar_conta(self, conta):
        conta_nao_existe = self._lista_conta.count(conta) == 0
        if conta_nao_existe:
            self._lista_conta.append(conta) 

    def listar_contas(self):
        for conta in self._lista_conta:
            print(conta.exibir_info())