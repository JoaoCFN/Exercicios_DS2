class Banco():
    def __init__(self, nome_banco, ano_fundacao):
        self.nome_banco = nome_banco
        self.ano_fundacao = ano_fundacao
        self._lista_agencias = []

    def adicionar_agencia(self, agencia):
        agencia_nao_existe = self._lista_agencias.count(agencia) == 0
        if agencia_nao_existe:
            self._lista_agencias.append(agencia) 
    
    def listar_agencias(self):
        for agencia in self._lista_agencias:
            print('''
                Número da agência: {}
                Lista de contas da agência: {}
            '''.format(
                agencia.numero,
                agencia.listar_contas()
            ))