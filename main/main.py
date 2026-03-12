import time
import sys
from funcoesDecisoes.mainDecisoes import *
from funcoesApoio.mainApoio import *
from ascii.ascii import mostrar_ascii


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
escrever("siga o caminho, ele te levara a um lugar seguro.")
time.sleep(4)

escrever("Você quer seguir o caminho que a voz mandou?")
time.sleep(2)

escrever("mas na mesma hora voce sente algo,")
escrever("esse nao é o caminho que voce quer seguir,")
escrever("seu caminho é pro outro lado")

escolha = input(
    "\n voce quer seguir o caminho que a voz mandou (s/n):?  "
).lower()

if escolha =="s":
    caminhoAlt()

elif escolha == "n":

    escrever("voce segue um caminho, mas parece que a floresta nao ta gostando muito.")
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
        time.sleep(1)
        escrever("eu nao sou tão assustadora assim,")
        time.sleep(1)
        escrever("olha pra tras, eu prometo que nao vou te machucar'")
        time.sleep(4)

        escolha = input("\n voce quer olhar pra tras? (s/n):?  ").lower()
        time.sleep(2)

        if escolha == "s":

            escrever("-- voce ta com medo mas quer q isso acabe")
            time.sleep(1)
            escrever("-- voce olha pra tras .. --")
            time.sleep(3)

            escrever("-- voce ve uma figura,")
            time.sleep(1)
            escrever("mas nao consegue distinguir o que é")
            time.sleep(1)
            escrever("voce sente um arrepio,")
            time.sleep(1)
            escrever("e a figura desaparece --")
            time.sleep(4)

            escrever("a floresta: nao achei que voce fosse olhar")
            time.sleep(1)
            escrever("mas tudo bem,")
            time.sleep(1)
            escrever("so cuidado pq nao sou o unico aqui,")
            time.sleep(1)
            escrever("mas sou o unico que n quer te machucar")
            

            somDeGalhos()
            time.sleep(2)

        elif escolha == "n":

            escrever("ainda bem que voce nao olhou")
            time.sleep(1)
            escrever("ate eu tenho medo")
            time.sleep(2)

        escrever("voce continua andando")
        time.sleep(1)
        escrever("ta tudo quieto, muito quieto")
        time.sleep(1)
        escrever("mas fazem minutos desde a ultima voz")
        time.sleep(3)

        escrever("voce anda olhando pra todo canto")
        time.sleep(1)
        escrever("nao ve muita coisa")
        time.sleep(1)
        escrever("so varias e varias arvores")
        time.sleep(3)

        escrever("voce escuta de vez enquando barulhos de animais")
        time.sleep(1)
        escrever("mas nao tem nada?")
        time.sleep(1)
        escrever("voce nao ve nada, é estranho")
        time.sleep(4)

        escrever("voce passa por um lugar onde tem um lago")
        time.sleep(1)
        escrever("o lago é tão calmo que parece um espelho")
        time.sleep(3)

        escrever("voce olha pro lago e ve seu reflexo...")
        time.sleep(3)

        escrever("voce se ve, normal como sempre")
        time.sleep(1)
        escrever("nem parece q ja ta a horas na floresta andando")
        time.sleep(3)

        escrever("voce fica um tempo ali se olhando")
        time.sleep(1)
        escrever("parece ate que voce passava muito tempo aqui")
        time.sleep(1)
        escrever("voce se sente bem")
        time.sleep(4)

        escrever("esse lago?")
        time.sleep(1)
        escrever("ele me é familiar")
        time.sleep(1)
        escrever("nao sei explicar")
        time.sleep(1)

        escrever("voce olha em volta nas margens")
        time.sleep(1)
        escrever("e ve algo")
        time.sleep(3)

        escrever("uma pedra")
        time.sleep(1)
        escrever("mas nao uma pedra normal")
        time.sleep(1)
        escrever("ela tem um rosto esculpido")
        time.sleep(1)
        escrever("desenhado")
        time.sleep(1)
        escrever("parece um desenho de criança")
        time.sleep(4)

        escrever("quando voce percebe")
        time.sleep(1)
        escrever("voce lembra de algo")
        time.sleep(1)

        escrever("a silueta de uma criança")
        time.sleep(1)
        escrever("e de dois adultos")
        time.sleep(1)
        escrever("os 3 brincando no lago")
        time.sleep(5)

        escrever("é seus pais")
        time.sleep(1)

        escrever("voce sente uma saudade avassaladora")
        time.sleep(1)
        escrever("tirando o caminho")
        time.sleep(1)
        escrever("esse é o primeiro sentimento bom")
        time.sleep(1)
        escrever("que voce sente desde q acordou")
        time.sleep(6)

        escrever("a floresta: lembranças sao coisas poderosas")
        time.sleep(1)
        escrever("elas te dao força")
        time.sleep(3)

        escrever("a floresta: mas elas sempre vem juntas")
        time.sleep(1)
        escrever("de lembraças ruins")
        time.sleep(4)

        escrever("-- voce sente algo chegar perto de voce")
        time.sleep(1)
        escrever("mas voce esta paralisado de medo")
        time.sleep(3)

        escrever("dessa vez nao é a mesma presença de antes")
        time.sleep(1)
        escrever("essa tras raiva")
        time.sleep(1)
        escrever("dor")
        time.sleep(1)
        escrever("essa quer te machucar --")
        time.sleep(4)

        escrever("-- voce é inundado de lembranças ruins")
        time.sleep(1)
        escrever("a primeira vez que voce quase se afogou no lago... --")
        time.sleep(4)

        escrever("a vez onde voce tava correndo de um animal")
        time.sleep(1)
        escrever("e teve que se jogar no lago")
        time.sleep(1)
        escrever("voce ficou la por mais tempo que podia")
        time.sleep(4)

        escrever("voce sente a agua entrando")
        time.sleep(1)
        escrever("voce sem forças")
        time.sleep(1)
        escrever("sua visao embaçada")
        time.sleep(4)

        escrever("e do nada uma presença te puxa")
        time.sleep(1)
        escrever("voce ve por um flash")
        mostrar_ascii(r'C:\Users\marki\OneDrive\Documentos\GitHub\A-Floresta-Carmezin\main\ascii', "arteLago.txt")
        time.sleep(1)
        escrever("e apaga")
        time.sleep(3)

        imagemLago()
        
        
        escrever("voce volta a si mas dessa vez voce nao quer chegar em casa...")
        time.sleep(1)
        escrever("voce precisa chegar em casa")
        time.sleep(3)
        
        escolha = input(
            "\n voce sente que o caminho é logo após esse lago, voce quer atravessar o lago? (s/n):?  "
        ).lower()
        
        if escolha == "n":
            escrever("Você da meia volta e segue seu caminho de volta")
            time.sleep(1)
            escrever("mas algo está atrás de você")
            time.sleep(2)
            escrever("antes que você percebesse sua barriga começa a doer")
            time.sleep(3)
            escrever("um chifre de cervo está atravessando sua barriga")
            time.sleep(3)
            escrever("seu corpo perde as forças e cede")
            time.sleep(3)
            escrever("e sua ultima visão... o lago estranhamente familiar.")
            time.sleep(3)
            escrever("F I M", 0.4)          


        elif escolha == "s":
            escrever("voce segue o caminho, e ele te leva pra um lugar mais claro")
            time.sleep(1)
            escrever("esse caminho é mais facil de andar, tem menos arvores, e tem mais luz")
            time.sleep(1)
            escrever("ao longe voce percebe uma casa, velha mal trapilha mas voce lembra...")
            time.sleep(1)
            escrever("essa é a sua casa")
            time.sleep(3)
            
            escrever("voce chega na porta...")
            time.sleep(1)
            escrever("exita um pouco mas abre a porta, chegando la voce é inundado de memorias")
            time.sleep(1)
            escrever("dessa vez boas...")
            time.sleep(1)
            escrever(" voce olha em volta e ve algo, sua casa ta toda destruida mas tem algo que lhe chama atenção")
            time.sleep(1)
            escrever("um pedaço de chifre carmesin")
            time.sleep(4)
            
            escolha = input(
                "\n voce quer pegar o chifre? (s/n):?  "
            ).lower()
            
            if escolha == "s":
                escrever("voce pega o chifre, é dele, ele nao é esse espirito bom que lhe salvou, é algo mais")
                time.sleep(1)
                escrever("voce olha e ve seu quarto de infancia, tudo destruido, mas um sentimento de desconforto, incomodo lhe preenche")
                time.sleep(1)
                escrever("tem algo no armario, voce sabe que tem")

            elif escolha =="n":
                escrever("voce ignora o chifre, e vai direto para uma porta estranhamente familiar")
                time.sleep(1)
                escrever("voce olha e ve seu quarto de infancia, tudo destruido, mas um sentimento de desconforto, incomodo lhe preenche")
                time.sleep(1)
                escrever("tem algo no armario, voce sabe que tem")
                
                escolha = input(
                    "\n voce quer abrir o armario? (s/n):?  "
                ).lower()
                
                if escolha == "s":
                    escrever("voce ta meio recioso mas quer que isso acabe, voce nao aguenta mais esse desconforto")
                    time.sleep(1)
                    escrever("quando voce abre o armario...")
                    time.sleep(1)
                    escrever("... nada? nao tem nada, voce olha em volta incredulo e seu olhar cai na janela...")
                    time.sleep(1)
                    
                    escrever("voce olha pra fora e ve algo la, no fundo da floresta...")
                    time.sleep(1)
                    escrever("voce encara aquilo, voce nao sente so medo, voce sente desespero...")
                    time.sleep(1)
                    escrever("mas algo passa na sua cabeça, aquilo nao esta la fora?...")
                    time.sleep(1)
                    escrever("voce lembra algo a mais da sua vida, vidro é muito dual, ele pode ser transparente com voce")
                    time.sleep(1)
                    escrever("mas ele pode ser um espelho, e o que voce ta vendo la fora... ")
                    time.sleep(1)
                    escrever("esta atras de voce")
                    mostrar_ascii(r'C:\Users\marki\OneDrive\Documentos\GitHub\A-Floresta-Carmezin\main\ascii', "arte.txt")
                    time.sleep(1)
                    escrever("voce se vira, e ve aquilo, a coisa que te seguiu")
                    time.sleep(1)
                    escrever("a coisa que te fez sentir medo, a coisa que te fez sentir desespero")
                    time.sleep(1)
                    escrever("num ataque de adrenalina e desespero voce corre na direçao da janela e pula")
                    time.sleep(1)
                    escrever("voce cai no chao, se machuca, mas consegue fugir quebrando aquela imagem que lhe trazia medo")
                    time.sleep(1)
                    escrever("mas ela nao para, ela esta ali com voce, ela continua ali, mais perto, ela sempre esteve ali")
                    time.sleep(1)
                    escrever("voce corre pra floresta no intuito de fugir, voce corre como se nao ouvesse amanha")
                    time.sleep(1)
                    escrever("mas do nada... essa raiz sempre esteve aqui? voce tropeça e cai")
                    time.sleep(1)
                    escrever("olha pra tras e ele esta ali... se aproximando")
                    time.sleep(1)
                    escrever("como um instinto voce fica em posiçao fetal...")
                    time.sleep(1)
                    escrever("fecha os olhos e sente algo chegando perto de voce, voce nao encherga pq ta de olhos fechados")
                    time.sleep(1)
                    escrever("mas voce sabe que é uma mao, quando ta chegando perto voce olha")
                    time.sleep(1)
                    escrever("e em fraçao de segundos voce apaga...")
                    time.sleep(1)
                    escrever(". . .",0.6)
                    time.sleep(1)
                    escrever("voce abre os olhos, mas nao consegue se mexer, voce olha pra baixo...")
                    time.sleep(1)
                    escrever("um broto de arvore, ele tem a sua cara de desespero crescendo nele...")
                    time.sleep(1)
                    escrever("voce olha pra frente e ve um outro vulto...")
                    time.sleep(1)
                    escrever("outra criança correndo desesperada")
                    time.sleep(1)
                    escrever("voce algum dia pode ter sido unico, mas aqui... voce so é mais um")
                    time.sleep(1)
                    escrever("F I M", 0.4)

                elif escolha =="n":
                    escrever("você não quer")
                    time.sleep(3)
                    escrever("mas seu corpo instintivamente move para abrir a porta do armário") 
                    time.sleep(2)
                    escrever("quando voce abre o armario...")
                    time.sleep(1)
                    escrever("... nada? nao tem nada, voce olha em volta incredulo e seu olhar cai na janela...")
                    time.sleep(1)
                    
                    escrever("voce olha pra fora e ve algo la, no fundo da floresta...")
                    time.sleep(1)
                    escrever("voce encara aquilo, voce nao sente so medo, voce sente desespero...")
                    time.sleep(1)
                    escrever("mas algo passa na sua cabeça, aquilo nao esta la fora?...")
                    time.sleep(1)
                    escrever("voce lembra algo a mais da sua vida, vidro é muito dual, ele pode ser transparente com voce")
                    time.sleep(1)
                    escrever("mas ele pode ser um espelho, e o que voce ta vendo la fora... ")
                    time.sleep(1)
                    escrever("esta atras de voce")
                    mostrar_ascii(r'C:\Users\marki\OneDrive\Documentos\GitHub\A-Floresta-Carmezin\main\ascii', "arte.txt")
                    time.sleep(1)
                    escrever("voce se vira, e ve aquilo, a coisa que te seguiu")
                    time.sleep(1)
                    escrever("a coisa que te fez sentir medo, a coisa que te fez sentir desespero")
                    time.sleep(1)
                    escrever("num ataque de adrenalina e desespero voce corre na direçao da janela e pula")
                    time.sleep(1)
                    escrever("voce cai no chao, se machuca, mas consegue fugir quebrando aquela imagem que lhe trazia medo")
                    time.sleep(1)
                    escrever("mas ela nao para, ela esta ali com voce, ela continua ali, mais perto, ela sempre esteve ali")
                    time.sleep(1)
                    escrever("voce corre pra floresta no intuito de fugir, voce corre como se nao ouvesse amanha")
                    time.sleep(1)
                    escrever("mas do nada... essa raiz sempre esteve aqui? voce tropeça e cai")
                    time.sleep(1)
                    escrever("olha pra tras e ele esta ali... se aproximando")
                    time.sleep(1)
                    escrever("como um instinto voce fica em posiçao fetal...")
                    time.sleep(1)
                    escrever("fecha os olhos e sente algo chegando perto de voce, voce nao encherga pq ta de olhos fechados")
                    time.sleep(1)
                    escrever("mas voce sabe que é uma mao, quando ta chegando perto voce olha")
                    time.sleep(1)
                    escrever("e em fraçao de segundos voce apaga...")
                    time.sleep(1)
                    escrever(". . .",0.6)
                    time.sleep(1)
                    escrever("voce abre os olhos, mas nao consegue se mexer, voce olha pra baixo...")
                    time.sleep(1)
                    escrever("um broto de arvore, ele tem a sua cara de desespero crescendo nele...")
                    time.sleep(1)
                    escrever("voce olha pra frente e ve um outro vulto...")
                    time.sleep(1)
                    escrever("outra criança correndo desesperada")
                    time.sleep(1)
                    escrever("voce algum dia pode ter sido unico, mas aqui... voce so é mais um")
                    time.sleep(1)
                    escrever("F I M", 0.4)