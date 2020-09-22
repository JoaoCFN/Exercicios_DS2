from Cachorro import Cachorro
from Pessoa import Pessoa


def main():
    dog1 = Cachorro("Madruguinha", 3, 'M', 2.5, "Yorkshire", "Longo")
    print(dog1.obter_informacoes())
    print("Som do cão Madruguinha: ", dog1.emitir_som())
    for n in range(7):
        dog1.mover()
    print(dog1.obter_informacoes())
    dog1.comer()
    print(dog1.obter_informacoes())
    print("====================")

    pessoa1 = Pessoa("Seu Madruga", 65, 'M', 55.0, "Cidade do México", "Carpinteiro")
    print(pessoa1.obter_informacoes())
    print("Som do Seu Madruga: ", pessoa1.emitir_som())
    pessoa1.ocupacao = "Docente"
    print("Ocupação: ", pessoa1.ocupacao)
    pessoa1.ocupacao = "Vendedor de churros"
    print("Ocupação: ", pessoa1.ocupacao)


main()
