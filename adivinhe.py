# Importando uma biblioteca para gerar números aleatórios
import random

numero = random.randint(1,10) 

tentativas = 0

while True:
    palpite = int(input("Digite um numero entre 1 a 10: "))
    tentativas += 1

    if palpite == numero:
        print("Parabéns você acertou o número!...A resposta correta era:", numero, ".Você tentou:", tentativas, "vezes") # Apresenta resultado de vitória e encerra o loop
        break
    else:
        print("VOCÊ ERROU!... Tente novamente.") # Apresenta a frase de derrota e reinicia o loop