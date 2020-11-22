class Voo:
    num_voo = 999

    def __init__(self, origem, destino, *escala):
        self.origem = origem
        self.destino = destino
        self.escala = escala
        Voo.num_voo += 1
    
    def get_taxa(self):
        taxa_total = self.origem.taxa_aeroporto + self.destino.taxa_aeroporto 
        for escala in self.escala:
            taxa_total += escala.taxa_aeroporto
        return taxa_total

    def get_info_voo(self):
        info = "Nº Vôo: {} \nOrigem: {} \nEscala:".format(self.origem, self.destino)
        if(len(self.escala) > 0):
            for escala in self.escala:
                info += "{}, ".format(escala)