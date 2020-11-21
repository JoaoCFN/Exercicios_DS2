class Reserva:
    num_reserva = 999

    def __init__(self, voo, classe = "X"):
        self.voo = voo
        self.classe = classe
        Reserva.num_reserva += 1
    
    def get_preco_final(self):
        classeConvUpper = self.classe.upper()
        valorTotal = 0

        if classeConvUpper == "X":
            valorTotal = voo.get_taxa() + 200 
            return valorTotal

        return voo.get_taxa()

    def get_info_reserva(self):
        returnText = "Dados do vôo: \n {} \nClasse: {} \nNúmero da reserva: {}\nPreço final (R$): {} \n".format(voo.get_info_voo(), self.classe, Reserva.num_reserva, self.get_preco_final())