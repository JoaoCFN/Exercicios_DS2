from Produto import Produto
class Churros(Produto):
    sabores = ["Doce de Leite", "Chocolate", "Goiabada"]
    _preco_base = 2.5 

    def __init__(self, sabor, tamanho, tem_cobertura):
        super().__init__("Churros", Churros.sabores[sabor], tamanho, Churros._preco_base)
        self.tem_cobertura = tem_cobertura
    
    @property
    def tem_cobetura(self):
        return self.tem_cobertura
    
    @tem_cobetura.setter
    def tem_cobetura(self, decisao):
        decisao_conv = str(decisao).upper()
        if decisao_conv == "S":
            self._tem_cobertura = "Sim"
            self._preco_base += 0.2
        else:
            self._tem_cobertura = "Não"

    def info(self):
        return super().info() + "\nTem cobertura: {}".format(self.tem_cobertura)  
