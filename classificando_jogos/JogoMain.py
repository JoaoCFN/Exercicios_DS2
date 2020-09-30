from Jogo import Jogo
from JogoCartas import JogoCartas
from JogoEletronico import JogoEletronico

def main():
    jogo1 = Jogo("Dominó", 0, 2, 20.00)
    jogo2 = JogoCartas("Yu-Gi-Oh", 12, 40.00, 2, ["Dark Hole", "Exodia", "Mirror Force", "Slifer"])
    jogo3 = JogoEletronico("GTA V", 18, 150.00, "Aventura", ["Windows", "PlayStation", "XBox"])

    print("="*20)
    print(jogo1.dados_jogo())
    print("="*20)
    print(jogo2.dados_jogo())
    print("="*20)
    print(jogo3.dados_jogo())
    print("="*20)
main()