import forca
import Adivinhacao

print("********************************")
print("      Bem Vindo aos jogos!      ")
print("********************************")

print("Escolha o jogo que deseja jogar: \n(1) Forca\n(2) Adivinhacão")

jogo = int(input("Escolha: "))

if (jogo == 1):
    forca.jogar()
elif (jogo == 2):
    Adivinhacao.jogar()


