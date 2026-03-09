import time
import sys
from funcoesDecisoes.mainDecisoes import *
from funcoesApoio.mainApoio import *


def escrever(texto, delay=0.02):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def titulo():
    escrever("""
=================================
        FLORESTA CARMESIM
=================================
""",0.001)
    time.sleep(1)


def inicio():
    escrever("\nVocê sente o cheiro de terra molhada.")
    time.sleep(3)

    escrever("Uma floresta infinita se estende ao seu redor.")
    time.sleep(3)

    escrever("Você não lembra de quem é... nem de onde veio.")
    time.sleep(3)

    escrever("Mas algo dentro de você mostra o caminho...")
    escrever("sera que é a casa?\n")
    time.sleep(3)


titulo()

while True:

    escolha = input("Você quer jogar? (s/n): ").lower()

    if escolha == "s":
        break

    elif escolha == "n":
        escrever("\na vida é feita de escolhas... mas nao dessa vez.")
        time.sleep(2)
        break

    else:
        escrever("Digite apenas 's' ou 'n'.")


inicio()

escrever("\nA floresta observa... mas ela tambem fala\n")
time.sleep(2)

escrever("A floresta: 'Bem-vindo, estranho. Voce esta perdido?'")
time.sleep(3)

escrever("-- o menino olha em volta assustado, mas nao ve ninguem --")
time.sleep(3)

escrever("A floresta: 'Nao se preocupe, voce nao esta seguro aqui.")
escrever("siga o caminho, ele te levara a um lugar seguro.'")
time.sleep(4)

escrever("Você quer seguir o caminho que a voz mandou?")
time.sleep(2)

escrever("mas na mesma hora voce sente algo,")
escrever("esse nao é o caminho que voce quer seguir,")
escrever("seu caminho é pro outro lado")

escolha = input(
    "\n voce quer seguir o caminho que a voz mandou (s/n):?  "
).lower()


if escolha == "s":

    escrever("voce segue um caminho, mas parece q a floresta nao ta gostando muito.")
    time.sleep(3)

    escrever("o caminho fica mais escuro, e mais silencioso,")
    escrever("voce sente que tem algo te seguindo, mas nao tem ninguem ali.")
    time.sleep(4)

    escrever("de algum lugar voce lembra isso")
    escrever("'quando a floresta fica em silencio, ela esta te observando,")
    escrever("ou pior, ela esta te caçando'")
    time.sleep(5)

    escolha = input(
        "\n voce sente medo, pq nao seguiu a floresta?\n"
        " voce valoriza tanto seu coraçao? pq?\n"
        " voce nem sabe quem voce é,\n"
        " voce olha pro lado e ve um lugar mais claro,\n"
        " voce sente que algo quer que voce va la\n"
        " mas voce nao quer ir pra la,\n"
        " pelo menos voce sente que nao é seu caminho,\n\n"
        " voce quer ir pra parte com luz? (s/n):?  "
    ).lower()

    if escolha == "n":

        escrever("é engraçado, voce me parece alguem muito corajoso")
        time.sleep(3)

        escrever("digo, voce ta numa floresta onde voce nao sabe oq ta atras de voce")
        time.sleep(3)

        escrever("tem algo atras de voce, voce nao quer olhar, mas voce sente")
        time.sleep(3)

        escrever("a floresta: 'voce tem medo de olhar pra tras?")
        escrever("eu nao sou tão assustadora assim,")
        escrever("olha pra tras, eu prometo que nao vou te machucar'")
        time.sleep(4)

        escolha = input("\n voce quer olhar pra tras? (s/n):?  ").lower()
        time.sleep(2)

        if escolha == "s":

            escrever("-- voce ta com medo mas quer q isso acabe")
            escrever("-- voce olha pra tras .. --")
            time.sleep(3)

            escrever("-- voce ve uma figura,")
            escrever("mas nao consegue distinguir o que é")
            escrever("voce sente um arrepio,")
            escrever("e a figura desaparece --")
            time.sleep(4)

            escrever("a floresta: nao achei que voce fosse olhar")
            escrever("mas tudo bem,")
            escrever("so cuidado pq nao sou o unico aqui,")
            escrever("mas sou o unico que n quer te machucar")

            somDeGalhos()
            time.sleep(2)

        elif escolha == "n":

            escrever("ainda bem que voce nao olhou")
            escrever("ate eu tenho medo")
            time.sleep(2)

        escrever("voce continua andando")
        escrever("ta tudo quieto, muito quieto")
        escrever("mas fazem minutos desde a ultima voz")
        time.sleep(3)

        escrever("voce anda olhando pra todo canto")
        escrever("nao ve muita coisa")
        escrever("so varias e varias arvores")
        time.sleep(3)

        escrever("voce escuta de vez enquando barulhos de animais")
        escrever("mas nao tem nada?")
        escrever("voce nao ve nada, é estranho")
        time.sleep(4)

        escrever("voce passa por um lugar onde tem um lago")
        escrever("o lago é tão calmo que parece um espelho")
        time.sleep(3)

        escrever("voce olha pro lago e ve seu reflexo...")
        time.sleep(3)

        escrever("voce se ve, normal como sempre")
        escrever("nem parece q ja ta a horas na floresta andando")
        time.sleep(3)

        escrever("voce fica um tempo ali se olhando")
        escrever("parece ate que voce passava muito tempo aqui")
        escrever("voce se sente bem")
        time.sleep(4)

        escrever("esse lago?")
        escrever("ele me é familiar")
        escrever("nao sei explicar")

        escrever("voce olha em volta nas margens")
        escrever("e ve algo")
        time.sleep(3)

        escrever("uma pedra")
        escrever("mas nao uma pedra normal")
        escrever("ela tem um rosto esculpido")
        escrever("desenhado")
        escrever("parece um desenho de criança")
        time.sleep(4)

        escrever("quando voce percebe")
        escrever("voce lembra de algo")

        escrever("a silueta de uma criança")
        escrever("e de dois adultos")
        escrever("os 3 brincando no lago")
        time.sleep(5)

        escrever("é seus pais")

        escrever("voce sente uma saudade avassaladora")
        escrever("tirando o caminho")
        escrever("esse é o primeiro sentimento bom")
        escrever("que voce sente desde q acordou")
        time.sleep(6)

        escrever("a floresta: lembranças sao coisas poderosas")
        escrever("elas te dao força")
        time.sleep(3)

        escrever("a floresta: mas elas sempre vem juntas")
        escrever("de lembraças ruins")
        time.sleep(4)

        escrever("-- voce sente algo chegar perto de voce")
        escrever("mas voce esta paralisado de medo")
        time.sleep(3)

        escrever("dessa vez nao é a mesma presença de antes")
        escrever("essa tras raiva")
        escrever("dor")
        escrever("essa quer te machucar --")
        time.sleep(4)

        escrever("-- voce é inundado de lembranças ruins")
        escrever("a primeira vez que voce quase se afogou no lago... --")
        time.sleep(4)

        escrever("a vez onde voce tava correndo de um animal")
        escrever("e teve que se jogar no lago")
        escrever("voce ficou la por mais tempo que podia")
        time.sleep(4)

        escrever("voce sente a agua entrando")
        escrever("voce sem forças")
        escrever("sua visao embaçada")

        escrever("e do nada uma presença te puxa")
        escrever("voce ve por um flash")
        escrever("e apaga")

        imagemLago()

    elif escolha == "s":
        caminho2()


elif escolha == "n":
    caminho1()