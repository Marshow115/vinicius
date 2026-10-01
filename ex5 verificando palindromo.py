'''
Verificar palíndromo
Escreva um programa que verifica se uma string é um palíndromo.
'''

frase = input("Digite uma frase: ").lower()
frase_sem_espaco = frase.replace(" ", " ")

if frase_sem_espaco == frase_sem_espaco[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
