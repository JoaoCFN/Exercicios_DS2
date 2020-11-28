class Reserva:
    contador_reserva = 999

    def __init__(self, voo, classe = "X"):
        self.voo = voo
        self.classe = classe
        Reserva.contador_reserva += 1
        self.num_reserva = Reserva.contador_reserva
    
    def get_preco_final(self):
        classeConvUpper = self.classe.upper()
        valorTotal = 0

        if classeConvUpper == "X":
            valorTotal = self.voo.get_taxa() + 200 
            return valorTotal

        return self.voo.get_taxa()

    def get_info_reserva(self):
        nome_classe = ""
        if self.classe.upper() == "X": 
            nome_classe = "Executiva"
        else: 
            nome_classe = "Econômica"

        info_reserva = "{} \nClasse: {} \nPreço final (R$): {} \n".format(self.voo.get_info_voo(), nome_classe, self.get_preco_final())

        return info_reserva