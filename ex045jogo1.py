# Crie um programa que faça o computador jogar Jokenpô com você.
print('\n========== DESAFIO 45 ==========\n')
from random import choice
from time import sleep

lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(lista)

print('=' * 50 )
print(f'{'JOGO DO JOKENPÔ':^50}')
print('=' * 50)
print("""1 - PEDRA
2 - PAPEL 
3 - TESOURA""")
print('=' * 50)
jogador = int(input('Tenta me ganhar... Qual sua escolha? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')

if jogador == 1:
    print(f'PEDRA X {computador}')
elif jogador == 2:
    print(f'PAPEL X {computador}')
elif jogador == 3:
    print(f'TESOURA X {computador}')
else:
    print('Opção inválida')


if computador == 'PEDRA':
    if jogador == 1:
        print('Deu EMPATE...')
    elif jogador == 2:
        print('Você GANHOU! Parabéns, jogou bem')
    elif jogador == 3:
        print('Você PEDEU! Hahaha mais sorte na próxima')
elif computador == 'PAPEL':
    if jogador == 2:
        print('Deu EMPATE...')
    elif jogador == 3:
        print('Você GANHOU! Parabéns, jogou bem')
    elif jogador == 1:
        print('Você PEDEU! Hahaha mais sorte na próxima')
elif computador == 'TESOURA':
    if jogador == 3:
        print('Deu EMPATE...')
    elif jogador == 1:
        print('Você GANHOU! Parabéns, jogou bem')
    elif jogador == 2:
        print('Você PEDEU! Hahaha mais sorte na próxima')