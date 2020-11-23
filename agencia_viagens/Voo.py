class Voo:
    num_voo = 99

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
        info_voo = "Nº Vôo: {} \nOrigem: {} | Destino: {}".format(Voo.num_voo, self.origem.nome, self.destino.nome)

        if(len(self.escala) > 0):
            info_voo += "| Escala: " 
            for escala in self.escala:
                info_voo += "{}, ".format(escala.nome)

        return info_voo