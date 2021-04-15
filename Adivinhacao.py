import random

print("********************************")
print("Bem Vindo ao jogo de Adivinhacao")
print("********************************")

numero = random.randrange(1, 101)
tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil \n(2) Médio \n(3) Difícil\n")

nivel = int(input("Nível: "))

if (nivel == 1):
    tentativas = 20
elif (nivel == 2):
    tentativas = 10
else:
    tentativas = 5

for rodada in range(1, tentativas + 1):
    print("------------------")
    print("  RODADA: {} de {}".format(rodada, tentativas))
    print("------------------")

    numero_usuario = int(input("Digite um número entre 1 e 100: "))

    if (numero_usuario < 1 or numero_usuario > 100):
        print("Número inválido! Tente novamente")
        continue

    if (numero_usuario == numero):
        print("Voce acertou!")
        break
    else:
        if (numero_usuario > numero):
            print("Voce chutou maior que número secreto!")
        elif (numero_usuario < numero):
            print("Voce chutou menor que o número secreto!")

        pontos = pontos - (abs(numero - numero_usuario))

print("Fim do jogo!")
print("Total de pontos: " + str(pontos))
