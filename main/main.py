import time

def titulo():
    print("""
=================================
        FLORESTA CARMESIM
=================================
""")
    time.sleep(1)

def inicio():
    print("\nVocê sente o cheiro de terra molhada.")
    time.sleep(3)
    print("Uma floresta infinita se estende ao seu redor.")
    time.sleep(3)
    print("Você não lembra de quem é... nem de onde veio.")
    time.sleep(3)
    print("Mas algo dentro de você diz que existe um caminho de volta para casa.\n")

titulo()

while True:
    escolha = input("Você quer jogar? (s/n): ").lower()

    if escolha == "s":
        print("\nA floresta observa...\n")
        time.sleep(2)
        inicio()
        break

    elif escolha == "n":
        print("\nTalvez seja melhor não entrar na floresta hoje...")
        break

    else:
        print("Digite apenas 's' ou 'n'.")