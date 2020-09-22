class Animal():
    def __init__(self,  nome, idade, genero, peso):
        self._nome = nome
        self._idade = idade
        self._genero = genero 
        self._peso = peso  
        self._energia = 60.0
        self.som = ""
    
    def obter_informacoes(self):
        return "Nome: {} | Idade: {} | Gênero: {} \nPeso: {:.2f} KG | Energia: {:.1f} %".format(self._nome, self._idade, self._genero, self._peso, self._energia)

    def comer(self):
        self._peso += 0.7
        if self._energia <= 75:
            self._energia += 25.0
        else: 
            self._energia = 100.0

    def mover(self):
        self._peso -= 0.1  
        if self._energia > 20:
            self._energia -= 10.0 
    
    def emitir_som(self):
        if self._energia > 10:
            self._energia -= 5.0
            return "{} \n".format(self.som)
        else:
            return ""