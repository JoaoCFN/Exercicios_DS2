class Produto():
    _preco_tamanho = [2.0, 2.5, 3.0]

    def __init__(self, nome, sabor, tamanho, preco_base):
        self._nome = nome  
        self._sabor = sabor  
        self._tamanho = tamanho  
        self._preco_base = preco_base 

    def preco(self):
        return _preco_base * _preco_tamanho[_tamanho]

    def info(self):
        return "Nome: {} \nSabor: {} \nTamanho: {} \nPreço {}".format(
            self._nome, self._sabor, self._tamanho, self.preco())