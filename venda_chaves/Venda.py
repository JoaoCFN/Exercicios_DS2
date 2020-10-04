class Venda():
    def __init__(self, itens, forma_pagamento):
        self._itens = itens
        self.forma_pagamento = forma_pagamento
    
    @property
    def forma_pagamento(self):
        return self._forma_pagamento
    
    @forma_pagamento.setter
    def forma_pagamento(self, pagamento):
        pagamento_conv = str(pagamento).upper()
        if pagamento_conv == "C":
            self._forma_pagamento = "Cartão"
        else:
            self._forma_pagamento = "Dinheiro"

    def calcular_preco_final(self):
        preco_final = 0
        for produto in self._itens:
            preco_final += produto.preco()
        
        if self.forma_pagamento == "Cartão":
            preco_final += (preco_final * 0.05)

        return preco_final

    def ler_itens(self):
        info_produtos = ""
        for produto in self._itens: 
            info_produtos += "{} \n".format(produto.info()) 
            
        return info_produtos
    
    def extrato_venda(self):
        extrato = "Itens Vendidos: {} \nPreço final da venda R$: {:.2f} \nForma de pagamento: {}".format(self.ler_itens(), self.calcular_preco_final(), self.forma_pagamento)

        return extrato