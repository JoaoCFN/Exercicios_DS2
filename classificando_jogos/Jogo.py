class Jogo():
    _tipo_jogo = ["Jogo Eletrônico", "Jogo de Cartas", "Outro"]

    def __init__(self, nome, clas_etaria, tipo, preco):
        self._nome = nome 
        self._clas_etaria = clas_etaria
        self._tipo = Jogo._tipo_jogo[tipo]
        self.preco = preco

    @property 
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        if self._clas_etaria >= 18:
            self._preco = novo_preco + (novo_preco * 0.1)
        elif self._clas_etaria >= 12 and self._clas_etaria < 18:
            self._preco = novo_preco + (novo_preco * 0.05)
        elif self._clas_etaria < 12:
            self._preco = novo_preco
    
    def dados_jogo(self):
        return "Nome: {} \nPreço R$: {} \nTipo do jogo: {}".format(
            self._nome, self.preco, self._tipo)