from Quadrado import Quadrado
from Circulo import Circulo
from math import sqrt, pi

def print_infos_circulo(circulo):
    print('''
        Dados do Circulo:
        Área: {}
        Circunferência: {}
    '''.format(circulo.obter_area(), circulo.obter_circunferencia()))

def GeometriaMain():
    quadrado1 = Quadrado(4)
    print('''
        Quadrado antes da atualização:
        Área: {}
        Perímetro: {}
        Diagonal: {}
    '''.format(quadrado1.obter_area(), quadrado1.obter_perimetro(), quadrado1.obter_diagonal()))

    Quadrado.atualizar_diag(sqrt(2))

    print('''
        Quadrado depois da atualização:
        Diagonal: {}
    '''.format(quadrado1.obter_diagonal()))

    circulo1 = Circulo(2.5)
    print_infos_circulo(circulo1)
    
    Circulo.atualizar_pi(pi)

    print('''
        Depois da atualização
    ''')
    
    print_infos_circulo(circulo1)

if __name__ == "__main__":
    GeometriaMain()
