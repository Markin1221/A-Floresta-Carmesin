import time
from funcoesDecisoes.mainDecisoes import *
from funcoesApoio.mainApoio import *

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
    print("Mas algo dentro de você mostra o caminho... sera que é a casa?\n")
    time.sleep(3)



titulo()

while True:
    escolha = input("Você quer jogar? (s/n): ").lower()

    if escolha == "s":
        
        break

    elif escolha == "n":

        print("\na vida é feita de escolhas... mas nao dessa vez.")
        time.sleep(2)
        break

    else:
        print("Digite apenas 's' ou 'n'.")
        
        
inicio()

print("\nA floresta observa... mas ela tambem fala\n")
time.sleep(2)

print("A floresta: 'Bem-vindo, estranho. Voce esta perdido?'")
time.sleep(3)

print("-- o menino olha em volta assustado, mas nao ve ninguem --")
time.sleep(3)
print("A floresta: 'Nao se preocupe, voce nao esta seguro aqui. siga o caminho, ele te levara a um lugar seguro.'")
time.sleep(4)
print("Você quer seguir o caminho que a voz mandou?")
time.sleep(2)
print("mas na mesma hora voce sente algo, esse nao é o caminho que voce quer seguir,seu caminho é pro outro lado")
escolha = input("\n voce quer seguir o caminho que a voz mandou (s/n):?  ").lower()
if escolha == "s":
    print("voce segue um caminho, mas parece q a floresta nao ta gostando muito.")
    time.sleep(3)
    print("o caminho fica mais escuro, e mais silencioso, voce sente que tem algo te seguindo, mas nao tem ninguem ali.")
    time.sleep(4)
    print("de algum lugar voce lembra isso 'quando a floresta fica em silencio, ela esta te observando, ou pior, ela esta te caçando'")
    time.sleep(5)
    escolha = input("\n voce sente medo, pq nao seguiu a floresta?\n voce valoriza tanto seu coraçao? pq? voce nem sabe quem voce é,\n voce olha pro lado e ve um lugar mais claro, voce sente que algo quer que voce va la\n mas voce nao quer ir pra la, pelo menos voce sente que nao é seu caminho,\n\n voce quer ir pra parte com luz? (s/n):?  ").lower()
    if escolha == "n":
       print("é engraçado, voce me parece alguem muito corajoso")
       time.sleep(3)
       print("digo, voce ta numa floresta onde voce nao sabe oq ta atras de voce ")
       time.sleep(3)
       print("tem algo atras de voce, voce nao quer olhar, mas voce sente")
       time.sleep(3)
       print("a floresta: 'voce tem medo de olhar pra tras? eu nao sou tão assustadora assim, olha pra tras, eu prometo que nao vou te machucar'")
       time.sleep(4)
       escolha = input("\n voce quer olhar pra tras? (s/n):?  ").lower()
       time.sleep(2)
       if escolha == "s":
           print("-- voce ta com medo mas quer q isso acabe, voce olha pra tras .. --")
           time.sleep(3)
           print("-- voce ve uma figura, mas nao consegue distinguir o que é, voce sente um arrepio, e a figura desaparece --")
           time.sleep(4)
           print("a floresta: nao achei que voce fosse olhar, mas tudo bem, so cuidado pq nao sou o unico aqui, mas sou o unico que n quer te machucar")
           somDeGalhos()
           time.sleep(2)
       elif escolha == "n":
           print("ainda bem que voce nao olhou ate eu tenho medo")
           time.sleep(2)
           
       print("voce continua andando, ta tudo quieto, muito quieto, mas fazem minutos desde a ultima voz")
       time.sleep(3)
       print("voce anda olhando pra todo canto, nao ve muita coisa so varias e varias arvores")
       time.sleep(3)
       print("voce escuta de vez enquando barulhos de animais mas nao tem nada? voce nao ve nada, é estranho")
       time.sleep(4)
       print("voce passa por um lugar onde tem um lago, o lago é tão calmo que parece um espelho") 
       time.sleep(3)
       print(", voce olha pro lago e ve seu reflexo...")
       time.sleep(3)
       print("voce se ve, normal como sempre, nem parece q ja ta a horas na floresta andando")
       time.sleep(3)
       print(" voce fica um tempo ali se olhando, parece ate que voce passava muito tempo aqui, voce se sente bem")
       time.sleep(4)
       print("esse lago? ele me é familiar, nao sei explicar, voce olha em volta nas margens e ve algo")
       time.sleep(3)
       print("uma pedra, mas nao uma pedra normal, ela tem um rosto esculpido, desenhado, parece um desenho de criança")
       time.sleep(4)
       print("quando voce percebe, voce lembra de algo, a silueta de uma criança e de dois adultos, os 3 brincando no lago")
       time.sleep(5)
       print(" é seus pais, voce sente uma saudade avassaladora, tirando o caminho esse é o primeiro sentimento bom que voce sente desde q acordou")
       time.sleep(6)
       print("a floresta: lembranças sao coisas poderosas, elas te dao força")
       time.sleep(3)
       print("a floresta: mas elas sempre vem juntas de lembraças ruins")
       time.sleep(4)
       print("-- voce sente algo chegar perto de voce,mas voce esta paralisado de medo")
       time.sleep(3)
       print("dessa vez nao é a mesma presença de antes, essa tras raiva, dor, essa quer te machucar--")
       time.sleep(4)
       print("-- voce é inundado de lembranças ruins, a primeira vez que voce quase se afogou no lago...")
       time.sleep(4)
       print("a vez onde voce tava correndo de um animal e teve que se jogar no lago, voce ficou la por mais tempo que podia")
       time.sleep(4)
       print("voce sente a agua entrando, voce sem forças, sua visao embaçada, e do nada uma presença te puxa, voce ve por um flash e apaga")
       imagemLago()
    elif escolha == "s":
        caminho2()
elif escolha == "n":
    caminho1()