from Produto import Produto

class Refresco(Produto):
    sabores = ["Groselha", "Limão", "Tamarindo"]

    def __init__(self, sabor, tamanho, tem_acucar):
        super().__init__("Refresco", sabores[sabor], tamanho, 1.5)
        self.tem_acucar = tem_acucar
    
    @property
    def tem_acucar(self):
        return self._tem_acucar
    
    @tem_acucar.setter
    def tem_acucar(self, decisao):
        decisao_conv = str(decisao).upper()
        if decisao_conv == "S":
           _tem_acucar = "Sim"
        else:
            _tem_acucar = "Não"
    
    def info(self):
        return super().info() + "\nTem Açúcar: {}".format(self.tem_acucar)
        
