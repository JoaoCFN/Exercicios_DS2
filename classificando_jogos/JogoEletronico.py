from Jogo import Jogo
class JogoEletronico(Jogo):
    def __init__(self, nome, clas_etaria, preco, categoria, plataformas):
        super().__init__(nome, clas_etaria, 0, preco)
        self.categoria = categoria
        self.plataformas = plataformas
    
    def listar_plataformas(self):
        self.plataformas.sort()
        string_plataformas = ""
        for plataforma in self.plataformas:
            string_plataformas += "{}; ".format(plataforma)

        return string_plataformas

    def dados_jogo(self):
        return super().dados_jogo() + "\nCategoria: {} \nPlataformas: {}".format(self.categoria, self.listar_plataformas())