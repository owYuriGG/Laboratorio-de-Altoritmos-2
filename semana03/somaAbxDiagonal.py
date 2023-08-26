# Escreva um programa que calcule e imprima a soma de todos os elementos abaixo da diagonal principal de uma matriz.
def sum(matriz):
    sum = 0

    for line in range(len(matriz)):
        for colum in range(len(matriz)):
            if line > colum:
                sum += matriz[line][colum]
    return sum


def main():
    matriz = [
        [1, 1, 1, 1],
        [2, 1, 1, 1],
        [3, 4, 1, 1],
        [5, 6, 7, 1]
    ]

    sum_matriz = sum(matriz)
    print(sum_matriz)

main()
