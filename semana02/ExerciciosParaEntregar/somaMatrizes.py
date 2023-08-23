# Escreva uma função que recebe duas matrizes como entrada e retorna uma nova matriz que é a soma das duas matrizes. Ambas matrizes devem possuir o tamanho de 3 x 3.

def sum_matriz(matriz1, matriz2):
    matriz = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for line in range(len(matriz)):
        for colum in range(len(matriz[line])):
            matriz[line][colum] = matriz1[line][colum] + matriz2[line][colum]
    return matriz

def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matriz2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sum = sum_matriz(matriz, matriz2)
    print(sum)

main()
